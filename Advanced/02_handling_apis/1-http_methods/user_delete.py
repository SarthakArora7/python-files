import requests

url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/delete"

response = requests.delete(url)

print(f"Response Code: {response.status_code}")
print(f"Response: {response.json()}")