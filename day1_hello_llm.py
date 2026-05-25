import requests

import json

ollama_url = "http://localhost:11434/api/generate"

payload = {
    "model" : "mistral:latest",
    "prompt" : "A customer is angry about a late delivery. Acknowledge their frustration and offer help.",
    "stream" : False
}


response = requests.post(ollama_url, json=payload)

data = response.json()

print("llm response:")
print(data["response"])