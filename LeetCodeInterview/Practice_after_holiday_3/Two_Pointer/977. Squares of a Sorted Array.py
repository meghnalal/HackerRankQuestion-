'''
977. Squares of a Sorted Array
'''

'''
Given an integer array nums sorted in non-decreasing[increasing] order,
return an array of the squares of each number sorted in non-decreasing[increasing] order.
'''

nums = [-5,-3,-2,-1]

left = 0
right = len(nums) - 1
ans = [0] * len(nums)

# for i in range(len(nums) - 1, -1, -1):
#     if (nums[i] ** 2) < (nums[left] ** 2):
#         nums[i], nums[left] = nums[left],  nums[i]
#
#     ans[i] = nums[i] ** 2
#
#     print(i)

for i in range(len(nums) - 1, -1, -1):
    if (nums[right] ** 2) > (nums[left] ** 2):
        ans[i] = nums[right] ** 2
        right -=1
    else:
        ans[i] = nums[left] ** 2
        left +=1
