from playsound3 import playsound
import time
import asyncio
from win11toast import toast

def blink ():
    playsound('./blink.mp3')
    toast('Blink', audio={'silent': 'true'}, duration='short')
    print("Blink please " + time.ctime(time.time()))
    time.sleep(100)
    blink()

blink()