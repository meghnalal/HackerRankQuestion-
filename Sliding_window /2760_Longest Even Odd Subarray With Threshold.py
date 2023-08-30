"""

You are given a 0-indexed integer array nums and an integer threshold.

Find the length of the longest subarray of nums starting at index l and ending at index r (0 <= l <= r < nums.length)
that satisfies the following conditions:

nums[l] % 2 == 0 ---> first one needs to be even
For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2 ---> even odd even
For all indices i in the range [l, r], nums[i] <= threshold ---> needs to be less or equal to 5

"""

nums = [2,3,4,5]
threshold = 4


r = 0
ans = 0


for l in (range(len(nums))):

    if nums[l] % 2 == 0 and nums[l] <= threshold:
        r = l + 1
        while r < len(nums) and nums[r] % 2 != nums[r - 1] % 2 and nums[r] <= threshold:
                r += 1
        ans = max(ans, r - l)
print(ans)
