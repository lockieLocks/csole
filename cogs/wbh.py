import requests
import aiohttp
import asyncio

class wbh:
    def __init__(self):
        pass

    def wbh_standard(self):
        message = """
WBH/Webhook Commands ---------------------
wbh info          >> Get information about a webhook
wbh s             >> Send a single message to a webhook
wbh sp            >> Spam a webhook with messages
wbh delete        >> Delete a webhook
wbh keylogger     >> Build a keylogger that sends logs, a screenshot and a webcam capture to a webhook
wbh silent_keylogger >> Build a silent keylogger that sends logs to a webhook
------------------------------------------
"""
        print(message)

    def wbh_info(self):
        print("Program is asking for a webhook")
        webhook_raw = input("console//: \n")
        webhook = webhook_raw.strip()
        r = requests.get(webhook)
        if r.status_code in [200, 201, 202, 204]:
            print(f"Webhook is valid: {webhook}")
            data = r.json()
            for key, value in data.items():
                print(f"{key} >> {value}")
            input("\nPress Enter to continue...")
        else:
            input("Invalid webhook URL.\n\nPress Enter to continue...")

    def wbh_s(self):
        try:
            print("Program is asking for a webhook")
            webhook_raw = input("console//: ")
            webhook = webhook_raw.strip()
            print("Program is asking for a message to send")
            message = input("console//: ")
            payload = {"content": message}
            r = requests.post(webhook, json=payload)
            if r.status_code in [200, 201, 202, 204]:
                input("Message sent successfully...\n\nPress Enter to continue...")
            else:
                input("Failed to send message...\n\nPress Enter to continue...")
        except Exception as e:
            input(f"An error occurred: {e}...\n\nPress Enter to continue...")

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
                            input("Failed to send message... \n\nPress Enter to continue...")
                        else:
                            print(f"-{i+1}- Message sent successfully.")
                    input("Spamming completed... \n\nPress Enter to continue...")
            asyncio.run(spam_loop())
        except ValueError:
            input("Invalid number entered... \n\nPress Enter to continue...")
        except Exception as e:
            input(f"An error occurred: {e}... \n\nPress Enter to continue...")

    def wbh_delete(self):
        try:
            print("Program is asking for a webhook to delete")
            webhook_raw = input("console//: ")
            webhook = webhook_raw.strip()
            r = requests.delete(webhook)
            if r.status_code in [200, 201, 202, 204]:
                input("Webhook deleted successfully... \n\nPress Enter to continue...")
            else:
                input("Failed to delete webhook... \n\nPress Enter to continue...")
        except Exception as e:
            input(f"An error occurred: {e}... \n\n\Press Enter to continue...")