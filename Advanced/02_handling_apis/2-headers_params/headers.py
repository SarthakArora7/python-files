import requests

# Headers are key-value pairs sent in HTTP requests and responses that provide essential information about the request or the response. 

# Content-Type: This header indicates the media type of the resource being sent. For example, application/json specifies that the request or response body contains JSON data. This helps the server understand how to parse the incoming data and how the client should interpret the response.

# Authorization: This header is used to pass authentication credentials, such as tokens or API keys, to access protected resources. For example, Authorization: Bearer <token> is commonly used for OAuth 2.0 authentication.

# Accept: This header tells the server what content types the client is willing to accept in the response. For example, Accept: application/json indicates that the client expects a JSON response.

url = "https://api.freeapi.app/api/v1/kitchen-sink/status-codes"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {3480784397387}"
}

response = requests.get(url, headers=headers)

print(f"Response Code: {response.status_code}")
print(f"Response: {response.json()}")