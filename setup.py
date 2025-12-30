import os
import subprocess
import sys

print("Installing required packages...")
try:
    console_file = "csle.py"
    os.system("pip install requests aiohttp pynput pyautogui opencv-python")
    input("Packages installed successfully.\n\nPress Enter to continue...")
    subprocess.run([sys.executable, console_file])
except Exception as e:
    print(f"Error installing packages: {e}")
