# Working with advanced lists

#       0, 1, 2, 3, 4, 5, 6 these are the index
nums = [1, 3, 4, 7, 8, 9, 4]

# prints value index in array where number is 4
# print (nums.index(4))
# >> 2

# deletes a value based on index number provided
del nums[2]
# print (nums)
# >> [1, 3, 7, 8, 9, 4]

# inserts 10 at the 0 index spot
# scoots the rest of index after over
nums.insert (0, 10)
# print (nums)
# >> [10, 1, 3, 7, 8, 9, 4]

# inserts an another array at the 0 index spot
nums.insert(0,[1,2,3])
# print (nums)
# >> [[1, 2, 3], 10, 1, 3, 7, 8, 9, 4]

# makes an array from a range of numbers 0 to 10
nums = range(10)
# print nums
# >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for each value in array 0 to 10, increase it by 2nd power
nums = [x**2 for x in range(10)]
# print nums
# >> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# for each value in array 0 to 10, increase it by 2nd power
# if it's remainder is 0 when divided by 2 (or if even number)
nums = [x**2 for x in range(10) if x % 2 ==0]
print nums
