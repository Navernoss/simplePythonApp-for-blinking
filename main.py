from playsound3 import playsound
import time
import asyncio
from win11toast import toast

def blinkwithnotif (intv):
    playsound('./blink.mp3')
    toast('Blink', audio={'silent': 'true'}, duration='short')
    print("Blink please " + time.ctime(time.time()))
    time.sleep(intv)
    blinkwithnotif(intv)

def blinkwithoutnotif (intv):
    playsound('./blink.mp3')
    print("Blink please " + time.ctime(time.time()))
    time.sleep(intv)
    blinkwithoutnotif(intv)

print('Hello! It\'s programm for blinking\n')

intv = int(input("Enter interval: ")) * 60
choice = input("Do u want to have notification? (Y/N): ")

if choice == "Y" or choice == "N" or choice == "n" or choice == "y":
    if choice == "Y" or choice == "y":
        blinkwithnotif(intv)
    if choice == "N" or choice == "n":
        blinkwithoutnotif(intv)


time.sleep(5)