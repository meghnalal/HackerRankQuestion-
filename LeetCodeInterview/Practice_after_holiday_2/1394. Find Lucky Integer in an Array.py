'''
1394. Find Lucky Integer in an Array
'''

'''
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.
'''
from collections import defaultdict
nums = [2,2,3,4]

count = defaultdict(int)
result = -1
for num in nums:
    count[num] += 1
# another option
# for i,x in count.items():
#     if i == x:
#         result = max(result, i)
for i in count:
    if i == count[i]:
        result= max(result,i)

print(result)