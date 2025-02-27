"""
283. Move Zeroes
"""

'''
Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

nums = [0, 1, 0, 3, 12]

left = 0
right = 0
while right < len(nums):
    if nums[right] != 0 :
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
    right += 1
print(nums)
