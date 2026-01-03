import os

def ping_ip(ip):
    amount = input("Program is asking for number of ping attempts (default 1)\n\nconsole//: ")
    if amount.isdigit():
        count_flag = f"-c {amount}"
    else:
        count_flag = "-c 1"
    print(f"Pinging IP address: {ip}")
    response = os.system(f"ping {count_flag} {ip}")
    if response == 0:
        input(f"IP address {ip} is reachable.\n\nPress Enter to continue...")
    else:
        input(f"IP address {ip} is not reachable.\n\nPress Enter to continue...")
