import requests

url = "http://localhost:8000/chat"

query = {"query": "Investigate recent errors"}

response = requests.post(url, params=query)

print("AI Response:\n")
print(response.json()["response"])