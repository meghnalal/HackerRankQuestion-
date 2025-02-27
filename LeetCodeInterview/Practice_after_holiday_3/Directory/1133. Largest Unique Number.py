'''
1133. Largest Unique Number
'''

'''
Given an integer array nums, return the largest integer that only occurs once. 
If no integer occurs once, return -1.
'''
from collections import defaultdict

nums = [5,7,3,9,4,9,8,3,1]
count = defaultdict(int)
ans= -1
for i in nums:
    count[i] += 1

for z, y in count.items():
    if y == 1:
        ans= max(ans,z)

