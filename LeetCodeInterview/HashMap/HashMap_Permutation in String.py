'''
567. Permutation in String
'''

'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

sliding window of fixed window
'''
from collections import defaultdict
s= 'ab'
s2 = "a"
v=['a','b']

k=len(s)

count= defaultdict(int)
counts2 = defaultdict(int)
for i in s:
    count[i] += 1

left=0
for x in range(k):
        counts2[s2[left]] += 1
        left += 1
        if count == counts2:
            ans = True
            print(ans)
            break
ans= False
for z in range(k, len(s2)):
    counts2[s2[z]] += 1
    counts2[s2[z - k]] -= 1
    if counts2[s2[z-k]] <= 0:
        del counts2[s2[z-k]]
    if count == counts2:
        ans = True
        print(ans)
        break

#  can do on improvemnt to make it clean but yeah thats the same procedure