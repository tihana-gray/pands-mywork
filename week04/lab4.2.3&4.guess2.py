# Modifying the program in lab4.2.2.guess1.py
# the new program needs to tell the user if their guess is too high or too low
# each time they guess
# by putting an if statement inside the while loop

# Author: Tihana Gray

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else: # I know it can't be equal or too low, so it must be too high
        print("Too high")
    guess = int(input("Please guess again: "))

print("Well done! Yes, the number was", numberToGuess) 

# Extra: get the program to generate a random number between 0 and 100 to guess
# import the random module

import random
numberToGuess = random.randint(0, 100)
print ("Random number to guess is: ", numberToGuess)
