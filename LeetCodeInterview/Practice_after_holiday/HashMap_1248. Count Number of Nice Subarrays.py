'''
1248. Count Number of Nice Subarrays
'''

'''
Given an array of positive integers nums and an integer k. 
Find the number of subarrays with exactly k odd numbers in them.

For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2. 
The subarrays with 3 odd numbers in them are [1, 1, 2, 1] and [ 1, 2, 1, 1].
We can check if a number is odd by taking it mod 2. If x is odd, then x % 2 = 1.
'''

'''
basically convert the array in [1,1,0,1,1]
 -> now just do when sum === k '''
from collections import defaultdict
nums = [1, 1, 2, 1, 1]
k = 3
counts = defaultdict(int)
counts[0] = 1
ans= curr = 0

for num in nums:
    curr += num % 2
    if counts[curr - k] in counts:
        ans += counts[curr - k]
    counts[curr] += 1
print(ans)