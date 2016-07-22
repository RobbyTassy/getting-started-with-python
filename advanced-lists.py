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
