"""

given an array of integers and a target sum greater than zero,
find the total amount of contiguous subarrays that add up to the non-zero targetSum.
example: ([1,2,3,4,5], 7) will output 1 ([3,4])

"""
nums = [1,2,3,4,5]
targetsum = 7

l=0
sum = 0

for i in range(len(nums)):
    if sum < targetsum:
        sum += nums[i]
    while sum > targetsum:
        sum -= nums[l]
        l += 1
    if sum == targetsum:
        print(i - l)
