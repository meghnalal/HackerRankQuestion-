'''
Count Elements With Maximum Frequency

'''

'''
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
Input: nums = [1,2,2,3,1,4]
Output: 4
'''
from collections import defaultdict

nums = [1,2,2,3,1,4]
dictcount = defaultdict(int)
maxval = 0
current_max=0

for i in nums:
    dictcount[i] +=1

for x in dictcount:
    maxval= max(maxval,dictcount[x])
print(maxval)
# better way of doing this
# maxFreq = max(dictcount.values())

for z in dictcount:
    if dictcount[z] == maxval:
        current_max += dictcount[z]
print(current_max)