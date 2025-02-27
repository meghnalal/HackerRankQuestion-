'''
Example 4: Given an integer array nums and an integer k,
find the sum of the subarray with the largest sum whose length is k.
'''

k = 4
nums = [3, -1, 4, 12, -8, 5, 6]

curr = 0
left = 0
for right in range(k):
    curr += nums[right]
print(curr)

ans = curr

for i in range(k, len(nums)):
    curr += nums[i] - nums[i - k]
    ans= max(ans,curr)
print(ans)
