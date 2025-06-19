import requests

url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/put"

data = {
    "Oh": "Yes",
    "Extra": "Fun"
}

response = requests.put(url, json=data)

print(f"Response Code: {response.status_code}")
print(f"Response: {response.json()}")