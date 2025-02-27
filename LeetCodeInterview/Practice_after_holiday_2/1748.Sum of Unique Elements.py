'''
Sum of Unique Elements
'''

'''
You are given an integer array nums. The unique elements of an array are the 
elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
'''
from collections import defaultdict
nums = [1,2,4,2]

non_duplicate= defaultdict(int)
for num in nums:
    non_duplicate[num] += 1
sum=0
for i in non_duplicate:
    if non_duplicate[i] <= 1:
        sum += i
print(sum)