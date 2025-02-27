'''
560. Subarray Sum Equals K
'''

'''
This solution intalis prefix_sum with hashmap - good for subarray that are === k or === something 
Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
'''
from collections import defaultdict
nums = [1, 2, 1, 2, 1]
k = 3
'''
Because the array can have negative numbers, the same prefix can occur multiple times. 
We use a hash map counts to track how many times a prefix has occurred.

'''

dictionary = defaultdict(int)
dictionary[0] = 1
ans = 0
prefixsum = 0

for num in nums:
    prefixsum += num
    if prefixsum - k in dictionary:
        ans += dictionary[prefixsum-k]
    dictionary[prefixsum] += 1

print(ans)
'''ans += counts[prefixsum - k]'''