# Rolling dice game.

import random

# Define variables

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the die...")
    print ("The values are...")
    print (random.randint(min, max))
    print (random.randint(min, max))

    roll_again = input("Roll the die again? y/n ")
else:
    print("Thank you for playing")
