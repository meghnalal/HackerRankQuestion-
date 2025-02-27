'''
Unique Number of Occurrences
'''

'''
Given an array of integers arr, return true if the number of occurrences of 
each value in the array is unique or false otherwise
'''
from collections import defaultdict

arrs = [1,2]

count = defaultdict(int)

for arr in arrs:
    count[arr] +=1

if len(set(count.values())) == len(count):
    print(True)
else:
    print(False)

# return len(set(count.values())) == len(count