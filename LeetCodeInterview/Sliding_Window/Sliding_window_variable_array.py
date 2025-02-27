'''
Example 1: Given an array of positive integers nums and an integer k,
find the length of the longest subarray whose sum is less than or equal to k.
This is the problem we have been talking about above. We will now formally solve it.
'''

nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8

left= 0
right = 0
current_sum=0
ans=0
for right in range(len(nums)):
    current_sum += nums[right]

    if current_sum == k:
        ans=(max(right-left+1,ans))
        print(ans)
    while current_sum > k:
        current_sum -= nums[left]
        left += 1
    