'''

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
'''

''' return min length subarray >= target  '''

target = 7
nums = [2,3,1,2,4,3]

left = 0
curr = 0
len_array = len(nums)+1
for right in range(len(nums)):
    curr += nums[right]
    while curr >= target:
        curr -= nums[left]
        ans = min(len_array, right - left + 1)
        left += 1
if len_array == len(nums)+1:
    print(0)
else:
    print(len_array)

