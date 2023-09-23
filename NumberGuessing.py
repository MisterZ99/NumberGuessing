import random
import math
import time
import os

lower = 1
upper = -1
chances = 0
count = 0
guess = 0

while lower>=upper:
    lower = int(input("\t\tEnter Lower Bound: "))
    upper = int(input("\t\tEnter Upper Bound: "))

number_of_interest = random.randint(lower,upper)
chances = max(1,int((upper-lower)/2))

print("\n\t\tYou've only %d chances to guess!" %(chances))

time.sleep(1)

print("\t\tAre you ready?")

time.sleep(1)

print("\t\tGo!\n")

time.sleep(1)

while count<chances:
    guess = int(input("\t\tChance %d\n\t\tGuess the number: " %(count+1)))
    if(guess==number_of_interest):
        print("\t\tCongratulations!\n\t\tYou guessed the number!\n")
        break
    else:
        print("\t\tYou missed!\n\t\t%d attempts remaining!\n\n"%(chances-count-1))
    count+=1

if count==chances:
    print("\t\tYou die!\n\t\tHahahahahahah!")