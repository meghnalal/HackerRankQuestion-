'''
Largest Unique Number
'''

'''
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
'''

from collections import defaultdict
nums = [9,9,8,8]

counts = defaultdict(int)
for num in nums :
    counts[num] += 1
    if counts[num] > 1 :
        del counts[num]

if len(counts) > 0:
    print(max(counts.keys()))
else:
    print(-1)