"""
copyright Meghna lal
"""

'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2
'''

nums = [1]
k = 0

i = 0
j = 0
current_sum = 0
count = 0
if len(nums) == 1:
		 if nums[0] == k:
			 return 1
		 else:
			 return 0
while i < len(nums):
    current_sum += nums[i]

    if current_sum > k :
        current_sum -= nums[j]
        j += 1
    if current_sum == k:
        current_sum -= nums[j]
        count += 1
        j += 1
    if current_sum > k and i >= len(nums)-1 :
        break
    i += 1
print(count)

