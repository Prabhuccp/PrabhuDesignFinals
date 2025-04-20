import requests
import json

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

while True:
    prompt = input("Enter your prompt (or type 'exit' to quit): ")
    
    if prompt.lower() == "exit":
        print("Goodbye!")
        break

    data = {
        "model": "llama3",
        "prompt": prompt
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        print("Response:\n", response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
