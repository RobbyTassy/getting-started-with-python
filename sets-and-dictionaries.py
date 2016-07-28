# Create a set

items = {"arrow", "spear", "arrow", "arrow", "rock"}

# print set

print (items)
print (len(items))

if "rock" in items:
    print ("rock found!")

#Create an empty set
# resets your array list
items = set()

# now add these strings
items.add("cat")
items.add("dog")
items.add("fish")

print (items)

numbers1 = {1, 3, 5, 7}
numbers2 = {1, 3}

# issubset method runs parameter within called statement to check if
# parameter exists inside called array
if numbers2.issubset(numbers1):
    print("Is a subset")
