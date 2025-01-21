import serial
import os
import subprocess
import time
from subprocess import CREATE_NEW_CONSOLE
from dotenv import load_dotenv, dotenv_values
from pynput.keyboard import Key, Controller

# Setup the serial connection
isRunning = True
ser = serial.Serial("COM7")
keyboard = Controller()

# Load the .env vars
load_dotenv()
ip = os.getenv("MY_IP")
username = os.getenv("USERNAME").lower()
serverPort = os.getenv("SERVER_PORT")
thpracPath = os.getenv("TOUHOU_THPRAC")

# Powershell path
powershellPath = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"

# Variables for the serial
inputBytes = None
inputInt = 0


# Loop for macros
while isRunning:
    inputBytes = ser.read()
    inputInt = int.from_bytes(inputBytes, 'big')

    # Call macro based on switch entered
    match inputInt:
        case 1:
            # Mainly for my discord, type "~☆" and send message
            keyboard.type(" ~☆")
            keyboard.tap(Key.enter)

        case 2:
            # Open powershell
            subprocess.Popen(powershellPath, creationflags=CREATE_NEW_CONSOLE)

        case 3:
            # Open my server via ssh
            subprocess.Popen([powershellPath, f"ssh -p {serverPort} {username}@{ip}"], creationflags=CREATE_NEW_CONSOLE)

        case 4:
            # Via Geforce Experience, save an instant replay
            keyboard.press(Key.alt)
            keyboard.tap(Key.f10)
            keyboard.release(Key.alt)
            
        case 5:
            # Run Touhou thprac (only when playing Touhou)
            subprocess.Popen(thpracPath)
            
            # Automatically say yes to the prompts
            time.sleep(0.10)
            keyboard.tap(Key.enter)
            keyboard.tap(Key.enter)

        case 6:
            # Under construction
            print(6)

        case 7:
            # Under construction
            print(7)

        case 8:
            # Under construction
            print(8)

        case 9:
            # Under construction
            print(9)

        case 10:
            # Under construction
            print(10)
        


