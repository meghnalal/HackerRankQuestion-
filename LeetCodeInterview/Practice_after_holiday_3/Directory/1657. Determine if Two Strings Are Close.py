'''
1657. Determine if Two Strings Are Close
'''

'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


'''
from collections import Counter

word1 = "cabbba"
word2 = "abbccc"

if len(word1) !=  len(word2):
    print(False)


ans = False
c1 = Counter(word1)
c2 = Counter(word2)
if (c1.keys() == c2.keys() and sorted(c1.values()) == sorted(c2.values())):
    print(True)