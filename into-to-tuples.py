# This is our first tuple - Tuples are immutable which means you can not change
# their values after they have already been set. However, you can change the
# values of the tuples elemes to create a new tuple.

tup1 = ('physics', 'chemistry', 'biology', 2015, 2016)
tup2 = (1, 2, 3, 4, 5, 6, 7);

print ('This prints tupp[0] :', tup1[0])
print ('this prints tup2[1:5] :', tup2[1:5])

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows:

tup3 = tup1 + tup2
print (tup3)

# This is how you delete a tuple

del tup3
