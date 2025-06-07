import requests
from dotenv import load_dotenv
load_dotenv()

import os


API_TOKEN = os.getenv("API_TOKEN")
headers = {"Authorization": f"Bearer {API_TOKEN}"}
data = {"inputs": "Powiedz coś mądrego."}

response = requests.post(
    "https://api-inference.huggingface.co/models/gpt2",
    headers=headers,
    json=data,
)

print(response.status_code)
print(response.json())
