'''
 Longest Substring Without Repeating Characters
'''

'''
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
'''
from collections import defaultdict
s = "abcabcbb"

dict_s= defaultdict(int)
left=0
ans= 0
for right in range(len(s)):
    dict_s[s[right]] += 1
    while dict_s[s[right]] > 1 :
        dict_s[s[left]] -= 1
        left += 1
    ans = max(ans,right-left+1)