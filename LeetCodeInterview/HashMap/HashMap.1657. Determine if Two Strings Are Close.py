'''
1657. Determine if Two Strings Are Close
'''

'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, 
and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
'''
from collections import defaultdict
from collections import Counter
word1 = "cabbba"
word2 = "abbccc"

if len(word1) != len(word2):
    print( False)

else:
    c1 = Counter(word1)
    c2 = Counter(word2)

    # for 2 strings to be close they have to:

    # 1.
    # have the same number of repetitions (values),
    # they don't have to be the same character (key) necessarily

    # 2.
    # keys need to match because - task says: we can only
    # transform every occurrence of one existing character

    if (c1.keys() == (c2.keys())
            and sorted(c1.values()) == sorted(c2.values())):
        print(True)

    print(False)

