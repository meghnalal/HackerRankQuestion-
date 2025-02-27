'''
Checking for existence
'''

'''
Example 1: 1. Two Sum

Given an array of integers nums and an integer target, return indices of two 
numbers such that they add up to target. You cannot use the same index twice.

'''
nums = [3,2,4]
target = 6

dict = {}
''' puting position as value as that is what i need to return --- remeber also you can search keys but not value '''
for i in range(len(nums)):
    num=nums[i]
    complement = target - num
    if complement in dict:
        print[i,dict[complement]]
    dict[num] = i

print (-1,-1)