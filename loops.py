value = "cat picture is cat picture"

# find first index of this strings

i = value.find("picture")
print (i)

# find first index (of this string) after previous index
b = value.find("picture", i + 1)
print (b)

value = "ralph waldo emerson"

i = value.find("python")

if i != -1:
    # not found
    print ("string found")
else:
    print ("string not found")
