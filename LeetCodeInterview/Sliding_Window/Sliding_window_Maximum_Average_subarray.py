"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average
value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""

nums = [1, 12, -5, -6, 50, 3]
k = 4
curr_sum = 0
left=0
right = k
ans = float('-inf')
for i in range(left, k):
    curr_sum += nums[i]
ans = curr_sum

for right in range(right, len(nums)):
    curr_sum += nums[right]
    curr_sum -= nums[right-k]
    if ans < curr_sum:
        ans= curr_sum
print(ans/k)