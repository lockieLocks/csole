import requests

def ip_lookup_func(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        for key, value in data.items():
            print(f"{key}: {value}")
        input("\nPress Enter to continue...")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        input("\nPress Enter to continue...")