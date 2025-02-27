'''
205. Isomorphic Strings
'''

'''
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character, but a character may map to itself.
'''
from collections import defaultdict
s = "bbbaaaba"
t = "aaabbbba"

counts= defaultdict(int)
countt= defaultdict(int)

for s1, t1 in zip(s,t):
    if s1 in counts and counts[s1] != t1 or (t1 in countt and countt[t1] != s1):
        print( False)
    counts[s1] = t1
    countt[t1] = s1


