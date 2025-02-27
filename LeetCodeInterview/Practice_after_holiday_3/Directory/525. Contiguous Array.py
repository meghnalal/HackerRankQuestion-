'''
525. Contiguous Array
'''

'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.


Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''
from collections import defaultdict

nums = [1,1,1,0,0,]
zero,one = 0,0
res= 0
count = defaultdict(int)
for i, n in enumerate(nums):
    if n == 0:
        zero += 1
    else:
        one +=1
    if one - zero not in count:
        count[one- zero ] = i
    if one == zero:
        res= one + zero
    else:
        idx = count[one- zero]
        res = max(res, i - idx )
print(res)
