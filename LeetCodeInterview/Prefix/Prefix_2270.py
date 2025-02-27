'''Prefix 2270'''
'''You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.'''

nums = [10,4,-8,7]


'''Prefexi sum calculation'''
prefix=[nums[0]]
for  i in range(1 ,len(nums)):
    prefix.append(nums[i] + prefix[-1])
left_sum=0
right_sum=0
count =0
for i in range(len(nums) - 1):
    left_sum = prefix[i]
    right_sum = prefix[len(nums)-1]-prefix[i+1] +nums[i+1]
    if left_sum >= right_sum:
        count += 1
print(count)

''' Optimising'''

nums = [10,4,-8,7]
left=0
ans=0
total = sum(nums)
for i in range(len(nums) - 1):
    left += nums[i]
    right = total - left
    if left >= right:
        ans += 1
print(ans)