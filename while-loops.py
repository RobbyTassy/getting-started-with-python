# prints out 0, 1, 2, 3, 4

# while loop simply repeats as long as boolean condition is met

count = 0
while count < 5:
    print (count)
    count += 1 # this is the same as count = count + 1

# this how you would break a loop

'''
Break is used to exit for or while loop
'''

# prints out 0, 1, 2, 3, 4

count = 0

while True:
    print (count)
    count += 1
    if count >= 5:
        break

