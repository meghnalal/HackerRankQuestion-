'''
209. Minimum Size Subarray Sum
'''

'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
Subarray
A subarray is a contiguous non-empty sequence of elements within an array.

whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''

target = 11
nums = [1,2,3,4,5]


left = 0
current_sum = 0
'''
as it can never be more then the array lenght
len_array = len(nums)+1
'''
len_array = float('inf')
for right in range(len(nums)):
    current_sum += nums[right]
    while current_sum >= target:
        len_array = min(len_array, right - left + 1)
        current_sum -= nums[left]
        left += 1
        
'''
if len_array == len(nums)+1:
    len_array = 0
'''
if len_array == float('inf'):
    len_array = 0
print(len_array)