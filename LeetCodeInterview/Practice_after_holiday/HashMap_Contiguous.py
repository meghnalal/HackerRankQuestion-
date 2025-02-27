'''
Contiguous Array
'''

'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
'''
from collections import defaultdict

nums = [1,1,1,1,0,0,0]
counts = defaultdict(int)
zero, one = 0,0
res=0
diff_index = defaultdict(int) # count[1] - count[0] ->

for num in range(len(nums)):
    if nums[num] == 0:
        zero += 1
    else:
        one += 1
    if one - zero not in diff_index:
        diff_index[one-zero] = num
    if one == zero :
        res= one + zero
    else:
        idx = diff_index[one-zero]
        res= max(res,num- idx)