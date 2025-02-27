'''
Count Elements With Maximum Frequency
'''

'''
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
'''
from collections import defaultdict
nums = [1,2,3,4,5]

count= defaultdict(int)
maxnum=0
totalsum=0
for num in nums:
    count[num] += 1
    maxnum=max(maxnum,count[num])

for i in count:
    if count[i] == maxnum:
        totalsum += count[i]


