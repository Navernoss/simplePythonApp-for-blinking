from playsound3 import playsound
import time
import asyncio
from win11toast import toast

def blink (intv):
    playsound('./blink.mp3')
    toast('Blink', audio={'silent': 'true'}, duration='short')
    print("Blink please " + time.ctime(time.time()))
    time.sleep(intv)
    blink(intv)

print('Hello! It\'s programm for blinking\n')

intv = int(input("Enter interval: "))
blink(intv)

time.sleep(5)