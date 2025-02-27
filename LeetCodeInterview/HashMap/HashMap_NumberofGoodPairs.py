'''
Number of Good Pairs
'''

'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
'''
from collections import  defaultdict

nums = [1,2,3,1,1,3]

count= defaultdict(int)

for i in nums:
    count[i] += 1
pair= 0
for c in count:
    n= count[c]
    pair += n * (n-1) // 2


