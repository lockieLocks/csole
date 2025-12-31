import requests

def shorten_url():
    url = input(f"Program is asking for a URL to shorten\n\nconsole//: ").strip()
    try:
        r = requests.get(f"https://tinyurl.com/api-create.php?url={url}")
        print(f"\n[+] Short URL: {r.text}")
    except Exception as e:
        print(f"[x] Error: {e}")
    input("\nPress Enter to continue...")
