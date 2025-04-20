import requests
import json

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

# Ask for model once at the beginning
model = input("Enter the model name (e.g., llama3, llama3.1, mistral, etc.): ")

while True:
    prompt = input(f"[{model}] Enter your prompt (or type 'exit' to quit): ")

    if prompt.lower() == "exit":
        print("Exiting...")
        break

    data = {
        "model": model,
        "prompt": prompt
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        print("Response:\n", response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
