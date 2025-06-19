import requests

def get_user_data():
    url = "https://api.freeapi.app/api/v1/public/youtube/videos"
    response = requests.get(url)
    print(f"Response Status: {response.status_code}")
    print(f"Response Reason: {response.reason}")  # OK
    response = response.json()
    if response["success"] and "data" in response:
        return response
    else: 
         raise Exception("Failed to fetch data")
    
def main():
    try:
        response = get_user_data()
        data = response["data"]
        pages = data["totalPages"]
        kind = data["data"][3]["kind"]
        print(f"Total Pages: {pages} \nKind: {kind}")
        
    except Exception as e:
         print(str(e))

if __name__ == "__main__":
     main()