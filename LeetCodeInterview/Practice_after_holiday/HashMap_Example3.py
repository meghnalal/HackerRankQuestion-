'''

Given an integer array nums, find all the unique numbers x in nums that satisfy the following:
 x + 1 is not in nums, and x - 1 is not in nums.
'''

nums = [10,6,5,8]

nums=set(nums)
ans=[]
for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            ans.append(num)

