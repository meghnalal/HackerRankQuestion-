'''
Largest Unique Number
'''
'''
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
Input: nums = [5,7,3,9,4,9,8,3,1]
Output: 8
 
'''
from collections import defaultdict
nums = [9,9,8,8]

dictionary = defaultdict(int)
maxval=-1
for i in nums:
    dictionary[i] +=1

for z in dictionary:
    if dictionary[z] == 1:
        maxval = max(maxval,z)
print(maxval)
