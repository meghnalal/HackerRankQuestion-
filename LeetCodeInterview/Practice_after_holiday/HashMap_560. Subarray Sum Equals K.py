'''
560. Subarray Sum Equals K
'''

from collections import defaultdict
nums = [1, 2, 1, 2,1]
k = 3

counts = defaultdict(int)
counts[0] = 1
ans = curr = 0

for nums in nums:
    curr += nums
    ans += counts[curr-k]
    counts[curr] += 1
print(ans)