import requests

def post_user():
    url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/post"

    data = {
        "name": "Ippo",
        "game": "Boxing",
        "game_id": "006"
    }

    response = requests.post(url, json=data)
    print(f"Response: {response.status_code}")
    return response

def main():
    try:
        response = post_user()
        print(f"Response JSON: {response.json()}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()