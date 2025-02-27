'''
340. Longest Substring with At Most K Distinct Characters 🔒
'''

'''
Example 1: You are given a string s and an integer k. Find the length of the longest 
substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. 
The longest substring with at most 2 distinct characters is "ece".
'''
from collections import defaultdict

s = "eceba"
k = 2
counts = defaultdict(int)
left = 0
ans = 0
for right in range(len(s)):
    counts[s[right]] +=1
    while len(counts) > k :
        counts[s[left]] -= 1
        if counts[s[left]] == 0:
            del counts[s[left]]
        left += 1
    ans= max(ans, right-left+1)
print(ans)



