import aiohttp
import asyncio
import os
import time

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class Username_Tr:
    def __init__(self):
        pass
    async def track_username(self):
        print("WARNING: This feature is in beta and may not work as expected.")
        time.sleep(3)
        clear()
        username = input("Program is asking for a username to track\n\nconsole//: ").strip()
        platforms = {
    "Youtube": {
        "url": f"https://youtube.com/@{username}",
        "error_msg": "404 Not Found"
    },
    "Twitter (X)": {
        "url": f"https://twitter.com/{username}",
        "error_msg": "This account doesn't exist",
        "check_type": "text"
    },
    "Instagram": {
        "url": f"https://instagram.com/{username}",
        "error_msg": "Sorry, this page isn't available.",
        "check_type": "text"
    },
    "TikTok": {
        "url": f"https://tiktok.com/@{username}",
        "error_msg": "Couldn't find this account",
        "check_type": "text"
    },
    "Facebook": {
        "url": f"https://facebook.com/{username}",
        "error_msg": "This page isn't available",
        "check_type": "text+redirect"
    },
    "Reddit": {
        "url": f"https://reddit.com/user/{username}",
        "error_msg": "Sorry, nobody on Reddit goes by that name.",
        "check_type": "text"
    },
    "GitHub": {
        "url": f"https://github.com/{username}",
        "error_msg": "404 Not Found"
    },
    "Twitch": {
        "url": f"https://twitch.tv/{username}",
        "error_msg": "This channel is unavailable",
        "check_type": "text"
    },
    "Pinterest": {
        "url": f"https://pinterest.com/{username}",
        "error_msg": "Sorry, we couldn't find that one",
        "check_type": "text"
    },
    "LinkedIn": {
        "url": f"https://linkedin.com/in/{username}",
        "error_msg": "This page doesn't exist",
        "check_type": "text",
        "headers": {"User-Agent": "Mozilla/5.0"}
    },
    "Snapchat": {
        "url": f"https://snapchat.com/add/{username}",
        "error_msg": "Sorry, we couldn't find",
        "check_type": "text"
    },
    "Quora": {
        "url": f"https://quora.com/profile/{username}",
        "error_msg": "Page Not Found",
        "check_type": "text"
    },
    "Steam": {
        "url": f"https://steamcommunity.com/id/{username}",
        "error_msg": "The specified profile could not be found",
        "check_type": "text"
    }
}
        print(f"Tracking username: {username}\n")
        async with aiohttp.ClientSession() as sack:
            for platform, details in platforms.items():
                url = details["url"]
                error_msg = details["error_msg"]
                check_type = details.get("check_type", "status")
                try:
                    response = await sack.get(url, headers=details.get("headers", {"User-Agent": "Mozilla/5.0"}))
                    if check_type == "status":
                        if response.status == 200:
                            print(f"[+] {platform}: Found at {url}")
                        else:
                            print(f"[-] {platform}: Not Found")
                    elif check_type == "text":
                        if error_msg in await response.text():
                            print(f"[-] {platform}: Not Found")
                        else:
                            print(f"[+] {platform}: Found at {url}")
                    elif check_type == "text+redirect":
                        if error_msg in await response.text() or response.url != url:
                            print(f"[-] {platform}: Not Found")
                        else:
                            print(f"[+] {platform}: Found at {url}")
                except Exception as e:
                    print(f"[!] {platform}: Error occurred - {e}")
            input("\nTracking completed... Press Enter to continue...")

if __name__ == "__main__":
    tracker = Username_Tr()
    asyncio.run(tracker.track_username())