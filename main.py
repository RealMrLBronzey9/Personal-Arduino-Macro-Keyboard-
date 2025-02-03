import serial
import os
import subprocess
import time
from subprocess import CREATE_NEW_CONSOLE
from dotenv import load_dotenv
from pynput.keyboard import Key, Controller

# Setup the serial connection
isRunning = True
global ser
ser = serial.Serial("COM7", 9600, timeout=2)    # 2 second timeout
keyboard = Controller()


# Load the .env vars
load_dotenv()
ip = os.getenv("MY_IP")
username = os.getenv("USERNAME").lower()
serverPort = os.getenv("SERVER_PORT")
thpracPath = os.getenv("TOUHOU_THPRAC")
browserPath = os.getenv("BROWSER")

# Powershell path
powershellPath = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"

# Variables for the serial
inputBytes = None
inputInt = 0


# Loop for macros
while isRunning:
    # Try is for if the serial connection fails
    try:
        inputBytes = ser.read(1)
        inputInt = int.from_bytes(inputBytes, "big")

        # Call macro based on switch entered
        match inputInt:
            case 1:
                # Mainly for my discord, type "~☆" and send message
                keyboard.type(" ~☆")
                keyboard.tap(Key.enter)
                time.sleep(1)

            case 2:
                # Open powershell
                subprocess.run(["wt", "powershell"])
                time.sleep(1)

            case 3:
                # Open my server via ssh
                subprocess.run(["wt", "powershell", "-Command", f"ssh -p {serverPort} {username}@{ip}"])
                time.sleep(1)

            case 4:
                # Via Geforce Experience, save an instant replay
                keyboard.press(Key.alt)
                keyboard.tap(Key.f10)
                keyboard.release(Key.alt)
                time.sleep(1)
                
            case 5:
                # Run Touhou thprac (only when playing Touhou)
                subprocess.Popen(thpracPath)
                
                # Automatically say yes to the prompts
                time.sleep(0.5)
                keyboard.tap(Key.enter)
                keyboard.tap(Key.enter)
                time.sleep(1)

            case 6:
                # Open TryHackMe.com
                subprocess.run([browserPath, "https://tryhackme.com/r/dashboard"])
                time.sleep(1)

            case 7:
                # Under construction
                print(7)
                time.sleep(1)

    except:
        # Attempt to fix the serial connection
        ser = None
        while ser == None:
            try:
                ser = serial.Serial("COM7")
            except:
                continue

    



        


