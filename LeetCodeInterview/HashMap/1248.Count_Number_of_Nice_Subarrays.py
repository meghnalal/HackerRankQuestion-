
'''
 1248. Count Number of Nice Subarrays
'''

'''

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

if its odd 1 % 2


'''
from collections import defaultdict
nums = [2,2,2,1,2,2,1,2,2,2]

k = 2

dictionary = defaultdict(int)
dictionary[0] = 1
ans = 0
curr = 0

for num in nums:
 curr += num % 2
 if curr - k in dictionary:
  ans += dictionary[curr-k]
 dictionary[curr] += 1
print (ans)


''' what worked in code submission'''

counts = defaultdict(int)
counts[0] = 1
ans = curr = 0

for num in nums:
 curr += num % 2
 if curr - k in counts:
  ans += counts[curr - k]
 counts[curr] += 1

print (ans)
