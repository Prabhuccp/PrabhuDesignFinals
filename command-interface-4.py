import requests
import json

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

# Step 1: Get the first model and its prompt
first_model = input("Enter the first model name (e.g., llama3, mistral, etc.): ")

while True:
    first_prompt = input(f"[{first_model}] Enter your prompt (or type 'exit' to quit): ")

    if first_prompt.lower() == "exit":
        print("Exiting...")
        break

    # Request to first model
    first_data = {
        "model": first_model,
        "prompt": first_prompt
    }

    try:
        first_response = requests.post(url, headers=headers, data=json.dumps(first_data), stream=True)
        first_response.raise_for_status()
        
        full_response_1 = ""
        for line in first_response.iter_lines():
            if line:
                decoded = json.loads(line.decode("utf-8"))
                full_response_1 += decoded.get("response", "")

        print(f"\nResponse from [{first_model}]:\n{full_response_1}")

    except requests.exceptions.RequestException as e:
        print("An error occurred with the first model:", e)
        continue

    # Step 2: Send that response to second model (gemma:3b)
    second_model = "gemma3:1b"  # Adjust this to match your actual model from `ollama list`
    second_data = {
        "model": second_model,
        "prompt": full_response_1
    }

    try:
        second_response = requests.post(url, headers=headers, data=json.dumps(second_data), stream=True)
        second_response.raise_for_status()

        full_response_2 = ""
        for line in second_response.iter_lines():
            if line:
                decoded = json.loads(line.decode("utf-8"))
                full_response_2 += decoded.get("response", "")

        print(f"\nResponse from [{second_model}]:\n{full_response_2}\n")

    except requests.exceptions.RequestException as e:
        print("An error occurred with the second model:", e)
