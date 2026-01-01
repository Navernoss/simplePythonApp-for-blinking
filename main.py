from playsound3 import playsound
import time
import asyncio
from win11toast import toast

def empty_func(args):
    pass

def blinkwithnotif (intv):
    playsound('https://friendly-hedgehog-352.convex.cloud/api/storage/80e89801-30ac-45ba-9ad0-b0541b794563')
    toast('Blink', on_dismissed=empty_func, audio={'silent': 'true'})
    print("Blink please " + time.ctime(time.time()))
    time.sleep(intv * 60)
    blinkwithnotif(intv)

def blinkwithoutnotif (intv):
    playsound('https://friendly-hedgehog-352.convex.cloud/api/storage/80e89801-30ac-45ba-9ad0-b0541b794563')
    print("Blink please " + time.ctime(time.time()))
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
    
    

main()
input()