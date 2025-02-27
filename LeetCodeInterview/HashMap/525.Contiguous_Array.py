'''
525. Contiguous Array
'''

'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
'''
from collections import defaultdict
nums = [0,1,0]

# dictionary = defaultdict(int)
# ans= 0
# left=0
# for right in nums:
#
# print (ans)

dictionary = defaultdict(int)
n=len(nums)
n1=0
n0=0
dictionary[0] = -1
ans = 0
prefixsum = 0
maxLen=0
for num in range(n):
    n1 += nums[num]
    n0 = (num + 1) - n1
    if n1 - n0 in dictionary:
        maxLen = max(maxLen, num - dictionary[n1 - n0])
    else:
        dictionary[n1 - n0] = num

print(maxLen)