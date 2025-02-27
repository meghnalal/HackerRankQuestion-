''' Minimum Value to Get Positive Step by Step Sum'''

'''
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

if array is positive we return 1 apperently 
'''

nums = [2,3,5,-5,-1]

prefix=[nums[0]]

for i in range(1,len(nums)):
    prefix.append(nums[i] + prefix[-1])

if min(prefix) >= 1:
    print(1)
else:
    findmin=1-min(prefix)
    print(findmin)


''' more efficient way '''
nums = [2,3,5,-5,-1]
min_val = 0
total = 0

        # Iterate over the array and get the minimum step-by-step total.
for num in nums:
    total += num
    min_val = min(min_val, total)

        # We have to change the minimum step-by-step total to 1,
        # by increasing the startValue from 0 to -min_val + 1,
        # which is just the minimum startValue we want.
print( -min_val + 1)