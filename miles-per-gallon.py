# Calculating miles per gallon

print ("This program calculates miles per gallon.")

# Ask user for input

miles_driven = input("Enter miles driven: ")

# Convert user input into float number

miles_driven = float (miles_driven)

# Get gallons used from the user

gallons_used = input("Enter gallons used: ")

gallons_used = float (gallons_used)

# Calculate and print the answer

mpg = miles_driven / gallons_used

print ("Miles per gallon: %d " % (mpg))
