'''
Example 3: 713. Subarray Product Less Than K.

Given an array of positive integers nums and an integer k, return the number of subarrays
where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8.
The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

'''

''' nums = [10, 5, 2, 6], k = 100
 subarray product less then k= [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
 answer is 8
'''

nums = [10, 5, 2, 6]
k = 100

left = 0
curr = 1
ans=0
for right in range(len(nums)):
    curr *= nums[right]
    while curr >= k:
        curr //= nums[left]
        left +=1
    ans += right - left +1
print(ans)