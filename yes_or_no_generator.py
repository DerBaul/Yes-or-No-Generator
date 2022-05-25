import random
import os
import time

#Functions###############################
def spit_out():
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(2.5)

    print("__________________________________________________\n\n\n\n         {}\n\n\n__________________________________________________".format(answer))
    exit()

clear = lambda: os.system('cls')


#Setup###############################
split = 50
print(range(-5,5))
clear()


#Input###############################
while True:
    wish = input("How much do you want the answer to be Yes(5) or No(-5)\nType an number from -5 to 5: ")
    if not wish:
        clear()
        time.sleep(1)
        print("!!!Dude. Make an Input!!!")
        time.sleep(1)
        continue

    
    if  wish in ["-5", "-4","-3","-2","-1","0","1","2","3","4","5",]:
        wish = int(wish)
        clear()
        break
    clear()


#Decide what the answer will be###############################
time.sleep(1)
if wish < -4:
    wish += 5
elif wish > 4:
    split -= 5
split = split + (wish * 10)
answer = "No"
chance = random.randrange(0, 100)
if chance < split:
    answer = "Yes"


#Presentation###############################
if wish == 0:
    print("Really letting faith decide this one...")
    spit_out()

#So you... NO/YES
mood = ["this is should not show. Do want your heart tells you", "prefer", "want it to be", "hope its going to be", "really need it to be", "will try till its"]

wish_txt = "No"
if wish > 0:
    wish_txt = "Yes"
print("So you {} {}".format(mood[abs(wish)], wish_txt))
time.sleep(4)
clear()
time.sleep(1)
print("Your result is...")
spit_out()
