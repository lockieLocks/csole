import requests
import aiohttp
import asyncio

class wbh:
    def __init__(self):
        pass

    def wbh_info(self):
        print("Program is asking for a webhook")
        webhook_raw = input("console//: ")
        webhook = webhook_raw.strip()
        r = requests.get(webhook)
        if r.status_code in [200, 201, 202, 204]:
            print(f"Webhook is valid: {webhook}")
            data = r.json()
            for key, value in data.items():
                print(f"{key} >> {value}")
        else:
            print("Invalid webhook URL.")

    def wbh_s(self):
        print("Program is asking for a webhook")
        webhook_raw = input("console//: ")
        webhook = webhook_raw.strip()
        print("Program is asking for a message to send")
        message = input("console//: ")
        payload = {"content": message}
        r = requests.post(webhook, json=payload)
        if r.status_code in [200, 201, 202, 204]:
            input("Message sent successfully... Press Enter to continue...")
        else:
            input("Failed to send message... Press Enter to continue...")

    def wbh_sp(self):
        try:
            print("Program is asking for a webhook")
            webhook_raw = input("console//: ")
            webhook = webhook_raw.strip()
            print("Program is asking for text to spam")
            text = input("console//: ")
            print("Program is asking for number of times to spam")
            times = int(input("console//: "))
            payload = {"content": text}
            async def spam_loop():
                async with aiohttp.ClientSession() as sack:
                    for i in range(times):
                        s = await sack.post(webhook, json=payload)
                        if s.status not in [200, 201, 202, 204]:
                            input("Failed to send message... Press Enter to continue...")
                        else:
                            print(f"-{i+1}- Message sent successfully.")
                    input("Spamming completed... Press Enter to continue...")
            asyncio.run(spam_loop())
        except ValueError:
            input("Invalid number entered... Press Enter to continue...")
        except Exception as e:
            input(f"An error occurred: {e}... Press Enter to continue...")

    def wbh_delete(self):
        print("Program is asking for a webhook to delete")
        webhook_raw = input("console//: ")
        webhook = webhook_raw.strip()
        r = requests.delete(webhook)
        if r.status_code in [200, 201, 202, 204]:
            input("Webhook deleted successfully... Press Enter to continue...")
        else:
            input("Failed to delete webhook... Press Enter to continue...")