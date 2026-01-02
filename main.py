import time
import asyncio
from win11toast import toast
import winsound
import os
from playsound3 import playsound

def empty_func(args):
    pass

file_path = os.path.join(os.path.dirname(__file__), 'blink.mp3')

def blinkwithnotif (intv):
    playsound(file_path)
    toast('Blink', on_dismissed=empty_func, audio={'silent': 'true'}, on_click="Don't touch this toast notification")
    print(f"Blink please (Now: {time.ctime(time.time())})")
    time.sleep(intv * 60)
    blinkwithnotif(intv)

def blinkwithoutnotif (intv):
    playsound(file_path)
    print(f"Blink please (Now: {time.ctime(time.time())})")
    time.sleep(intv * 60)
    blinkwithoutnotif(intv)


def choiceMin():
    intv = input("Enter interval (in minutes): ")
    if intv.isnumeric():
        return int(intv)
    else:
        print("Your symbol isn't digit")
        choiceMin()

def choiceNot(intv):
    choice = input("Do you want notifications? (Y/N): ")

    if choice.isnumeric() != True:
        if choice == "Y" or choice == "N" or choice == "n" or choice == "y":
            if choice == "Y" or choice == "y":
                blinkwithnotif(intv)
            if choice == "N" or choice == "n":
                blinkwithoutnotif(intv)
        else:
            print("Your symbol isn't right\n")
            choiceNot(intv)
    else: 
        print("Your symbol isn't right\n")
        choiceNot(intv)

def main():
    print('Welcome to Blink Reminder!\n')
    intv = choiceMin()
    print(f'We will reminder you to blink every ' + str(intv) + " minutes!\n")
    choiceNot(intv)
    
    
try:
    main()
    input()
except KeyboardInterrupt:
    print("\nWork was stopped. Goodbye)")