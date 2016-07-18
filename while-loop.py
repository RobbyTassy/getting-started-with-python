# Sum from 1 to a given number

n = int(input("Enter your number to determine sum of 1 and your number: "))
i = 1
sum = 0

while i <= n:
    sum += i
    i += 1

print (sum)
