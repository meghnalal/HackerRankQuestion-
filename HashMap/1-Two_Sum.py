'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
nums = [2,11,7,15]
target = 9
num_to_index = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in num_to_index:
        print(num_to_index[complement], i)
    num_to_index[num] = i
    ''' num_to_index[num] = i  num is value and i is the corrisponding index  '''
