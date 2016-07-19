# This is our first number guessing game

import random

# defining variables

n = random.randint(1,10)

guess = int(input("Enter an integer from 1 to 10: "))

# Do a loop

while n  != "guess":
    if guess < n:
        print ("Your guess is too low")
        guess = int(input("Enter an integer from 1 to 10: "))
    elif guess > n:
        print ("Your guess is too high")
        guess = int(input("Enter an integer from 1 to 10: "))
    else:
        print ("You guessed correctly! It was %d!" % (guess))        
        break

    
