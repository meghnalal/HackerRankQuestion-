'''
example1
'''

'''

Given an array of positive integers nums and an integer k, find the length 
of the longest subarray whose sum is less than or equal to k. This is the 
problem we have been talking about above. We will now formally solve it.
'''
nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8.

left =0
ans= 0
currsum=0
for right in range(len(nums)):
    currsum += nums[right]
    while currsum > k:
        currsum -= nums[left]
        left += 1
    ans= max(ans, right-left +1 )

print(ans)
