'''

To explain why this algorithm works, let's look at a specific example. Let's say that we are given a positive integer
array nums and an integer k. We need to find the length of the longest subarray that has a sum less than or equal to k.
For this example, let nums = [3, 2, 1, 3, 1, 1] and k = 5.

'''

nums = [3, 2, 1, 3, 1, 1]
k = 5

left = 0
curr = 0
ans = 0
for right in range(len(nums)):
    curr += nums[right]
    while curr > k:
        curr -= nums[left]
        left += 1
    if curr == k:
       ans = max(ans, right - left + 1)
print(ans)
