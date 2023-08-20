"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average
value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
"""

'''method with iteration '''

nums = [1,12,-5,-6,50,3]
k = 4

sum_first= 0
sum_window = sum(nums[:k])

for i in range(len(nums)-k):
    new_sum = sum_window - nums[i] + nums[i+k]
    if new_sum > sum_window:
        sum_window = new_sum
print (sum_window/k)

''' with pointer method '''
#nums = [1,12,-5,-6,50,3]
nums = [-1]
k = 1
i = 0
j = 0
sum_try =float('-inf')
sum_initial= 0

while j < len(nums):
    sum_initial = sum_initial + nums[j]
    if j-i+1 == k :
        sum_initial = sum_initial + nums[j]
        if sum_try < sum_initial:
            sum_try = sum_initial
        j += 1
    if j-i+1 > k:
        sum_initial = sum_initial - nums[i]
        i += 1
print(sum_try/k)

'''Better readability to above code with pointers  by adding one by one to sum hence why its a bit slower'''
nums = [1,12,-5,-6,50,3]
k = 4
i = 0
j = 0
sum_initial = 0
sum_try = float('-inf')

while j < len(nums):
    sum_initial += nums[j]

    if j - i + 1 == k:
        sum_try = max(sum_try, sum_initial)
        sum_initial -= nums[i]
        i += 1

    j += 1

average_max = sum_try / k
print(average_max)

''' Better solution and better written also by me because it has sum and just adding and removing  '''
l = 0
r = k

initial_sum = sum(nums[:k])
initial_average = initial_sum / k
while r < len(nums):
    initial_sum = initial_sum - nums[l] + nums[r]
    average = initial_sum / k
    if average > initial_average:
        initial_average = average
    l += 1
    r += 1
print (initial_average)

