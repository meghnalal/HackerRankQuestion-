'''
Counting
'''

'''
Example 1: You are given a string s and an integer k. Find the length of the longest substring 
that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 
distinct characters is "ece".
'''
s = "eceba"
k = 2

dict={}

left=0
ans= 0
for right in range(len(s)):
    if s[right] not in dict:
        dict[s[right]] = 0
    dict[s[right]] += 1
    while len(dict) > k:
        dict[s[left]] -= 1
        if dict[s[left]] == 0:
            del dict[s[left]]
        left += 1
    ans = max(ans, right - left + 1)
print(ans)

''' apperently better dictionary'''
# from collections import defaultdict
# counts = defaultdict(int)
# left = ans = 0
# for right in range(len(s)):
#     counts[s[right]] += 1
#     while len(counts) > k:
#         counts[s[left]] -= 1
#         if counts[s[left]] == 0:
#             del counts[s[left]]
#         left += 1
#
#     ans = max(ans, right - left + 1)
#
# print(ans)