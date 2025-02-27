'''
Sum of Unique Elements
'''

'''
You are given an integer array nums. 
The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
Input: nums = [1,2,3,2]
Output: 4
'''
from collections import defaultdict

nums = [1,2,3,2]
count= defaultdict(int)
ans=0

for i in nums:
    count[i] += 1
for j in count:
    if count[j] == 1:
        ans += j
print(ans)

