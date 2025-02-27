'''
Find Lucky Integer in an Array
'''

'''
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
Return the largest lucky integer in the array. If there is no lucky integer return -1.
arr = [2,2,3,4]
'''
from collections import defaultdict

arr = [1,2,2,3,3,3]

defaultdict1 = defaultdict(int)

for i in arr :
    defaultdict1[i] += 1

lucky_number=-1
for x in defaultdict1:

    if x == defaultdict1[x]:
        lucky_number = max(x,lucky_number)
