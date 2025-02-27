'''
290. Word Pattern
'''

'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between 
a letter in pattern and a non-empty word in s.
'''

from collections import defaultdict
pattern = "abba"
s = "dog cat cat dog"
s_list = s.split()
if len(s) != len(s_list):
    print(False)

countpatter=defaultdict(int)
countstring= defaultdict(int)

for string1, pattern1 in zip(s_list,pattern):
    if (string1 in countstring and countstring[string1] != pattern1) or (pattern1 in countpatter and countpatter[pattern1] != string1):
        print(False)
    countstring[string1] = pattern1
    countpatter[pattern1] = string1
print(True)