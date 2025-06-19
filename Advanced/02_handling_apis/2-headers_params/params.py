import requests

# Used in GET requests to filter or sort data.

# Sent in the URL like: ...?page=2&limit=10.

url = "https://api.freeapi.app/api/v1/public/youtube/videos"

filter = {
    "page": 2,
    "limit": 5
}

response = requests.get(url, params=filter)

print(f"Response Code: {response.status_code}")

print(f"Response: {response.json()}")