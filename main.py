import serial
import os
from pynput.keyboard import Key, Controller

# Setup the serial connection
isRunning = True
ser = serial.Serial("COM7")
keyboard = Controller()

# Variables for the serial
inputBytes = None
inputInt = 0

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
            os.startfile("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe")

        case 3:
            # Via Geforce Experience, save an instant replay
            keyboard.press(Key.alt)
            keyboard.tap(Key.f10)
            keyboard.release(Key.alt)
            
        case 4:
            # Under construction
            print(4)
        
        case 5:
            # Under construction
            print(5)  

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
        


