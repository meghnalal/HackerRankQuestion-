'''
Contains Duplicate
'''

'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
Input: nums = [1,2,3,1]
Output: true
'''

nums = [1,2,3,1]

setnums= set(nums)

if len(setnums) == len(nums):
    print(False)
else:
    print(True)
