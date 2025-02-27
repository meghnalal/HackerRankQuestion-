'''
Sort Characters By Frequency
'''

'''
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
'''
from collections import defaultdict

s = "cccaaa"

count= defaultdict(int)

for i in s:
    count[i] += 1

sorted_by_keys = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}

res = ""

for k , v in sorted_by_keys.items():
    res += (k*v)
    print(k)

# if iit was an array
# s1 = ''.join(arr)

