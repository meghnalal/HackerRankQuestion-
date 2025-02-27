'''
930. Binary Subarrays With Sum
'''

'''
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.
'''
from collections import defaultdict
nums = [1,0,1,0,1]
goal = 2

counts = defaultdict(int)
counts[0] = 1
ans = curr = 0

for num in nums:
    curr += num
    ans += counts[curr - goal]
    counts[curr] += 1

print(ans)