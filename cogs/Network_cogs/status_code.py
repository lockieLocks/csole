import requests

def get_url_status(url):
    try:
        response = requests.get(url)
        if response.status_code in [200, 201, 202]:
            print(f"The URL is reachable. Status Code: {response.status_code}")
        else:
            input(f"Status Code >> {response.status_code}\n\nPress Enter to continue...")
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")