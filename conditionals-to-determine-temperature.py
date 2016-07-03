# Enter your name

name = raw_input ("What is your name? " )
print ("Hello " + name + "!")

# Enter your age

age = input ("What is your age? " )
print ("That's great, " + name + "!")

# Ask for temperature outisde

temperature = float(input("What is the temperature outside? "))
if temperature > 70:
    print ("Wear shorts today, " + name)
    print ("Enjoy your day!")
else:
    print ("Wear long pants today, " + name)
    print ("Enjoy your day!")
