"""
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student.
You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest
of the k scores is minimized.

Return the minimum possible difference.

Example:
    Input: nums = [9,4,1,7], k = 2
    Output: 2
    Explanation: There are six ways to pick score(s) of two students:
    - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
    - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
    - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
    - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
    - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
    - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
    The minimum possible difference is 2.
"""
''' sorted with slifing window no need to use pointers in my opinion '''
nums = [9, 4, 1, 7]
k = 3
nums.sort()
count = float('inf')

for i in range(len(nums)-k+1):
    difference = nums[i+k-1]-nums[i]
    if difference < count:
        count = difference
print(count)
