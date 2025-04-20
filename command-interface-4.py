import requests
import json

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

# Step 1: Ask for first model
first_model = input("Enter the FIRST model name (e.g., llama3, mistral): ")
second_model = "gemma:3.1b"

while True:
    prompt = input(f"[{first_model}] Enter your prompt (or type 'exit' to quit): ")

    if prompt.lower() == "exit":
        print("Exiting...")
        break

    def get_response_from_model(model_name, prompt_text):
        data = {
            "model": model_name,
            "prompt": prompt_text,
            "stream": True
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)
            response.raise_for_status()
            output = ""
            for line in response.iter_lines():
                if line:
                    json_data = json.loads(line.decode('utf-8'))
                    output += json_data.get("response", "")
            return output.strip()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while querying model {model_name}:", e)
            return ""

    # Step 2: Query first model
    first_output = get_response_from_model(first_model, prompt)
    print(f"\n[{first_model}] Response:\n{first_output}")

    # Step 3: Query second model with first model's response
    second_output = get_response_from_model(second_model, first_output)
    print(f"\n[{second_model}] Response to the first model's output:\n{second_output}\n")
