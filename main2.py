#!/usr/bin/env python3
import sys, random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
print("Hello, beep bop. I am Numberbot.")
number = random.randrange(1,51)
guess = -1
while guess != number:
    guess = input("Please guess a number between 1 and 50: ")
    try:
        guess = int(guess)
        if guess == int(number - 5):
            print("Close! Try again!") 
        elif guess == int(number - 4):
            print("Close! Try again!") 
        elif guess == int(number - 3):
            print("Close! Try again!") 
        elif guess == int(number - 2):
            print("Close! Try again!") 
        elif guess == int(number - 1):
            print("Close! Try again!") 
        elif guess == int(number + 5):
            print("Close! Try again!") 
        elif guess == int(number + 4):
            print("Close! Try again!") 
        elif guess == int(number + 3):
            print("Close! Try again!") 
        elif guess == int(number + 2):
            print("Close! Try again!") 
        elif guess == int(number + 1):
            print("Close! Try again!") 
        else:
            print("Beep beep beep. Not even close. Try again.")
    except:
        print("BEEEEEP! Numbers only!")
print("Beep bop boop! You got it!")