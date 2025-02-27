""" practice"""

'''
Given an array of integers nums, you start with an initial positive value startValue.
In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
Return the minimum positive value of startValue such that the step by step sum is never less than 1.
nums = [-3,2,-3,4,2]
Output: 5

'''

nums = [-3, 2, -3, 4, 2]
prefix = [nums[0]]

for i in range(1, len(nums)):
    prefix.append(nums[i] + prefix[-1])

if min(prefix) >= 1:
    print(1)
else:
    findmin = 1 - min(prefix)
    print(findmin)
