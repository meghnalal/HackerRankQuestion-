'''
1248. Count Number of Nice Subarrays
'''

'''
1248. Count Number of Nice Subarrays
Given an array of positive integers nums and an integer k. 
Find the number of subarrays with exactly k odd numbers in them.

For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2. 
The subarrays with 3 odd numbers in them are [1, 1, 2, 1, 1] and [1, 1, 2, 1, 1].
'''
from collections import defaultdict

count = defaultdict(int)
count[0]= 1
nums = [2,2,2,1,2,2,1,2,2,2]
countodd=0
k = 2
ans=0
for num in nums:
    countodd += num % 2
    ans += count[countodd-k]
    count[countodd] += 1
print(ans)