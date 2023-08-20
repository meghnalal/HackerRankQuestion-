"""
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example:
    Input: nums = [1,2,3,1], k = 3
    Output: true
"""
'''
condition = nums[i] == nums[j]
            abs(i - j) <= k
            
HINT k here is not the size of array its the differences between indices 

more of a hasmap or set solution 
'''

nums = [1,2,3,1]

k = 3
i = 0

window = set()

while i < len(nums):

    if nums[i] in window:
        print(True)

    window.add(nums[i])

    if i >= k:
        window.remove(nums[i - k])
    i += 1
print(False)