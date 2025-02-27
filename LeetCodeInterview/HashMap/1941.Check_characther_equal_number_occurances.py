'''

'''

'''
Given a string s, determine if all characters have the same frequency.

For example, given s = "abacbc", return true. 
All characters appear twice. Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
'''

s = "abacbc"

dict={}

for i in s:
    if i not in dict:
        dict[i] = 0
    dict[i] += 1
print(dict)

# value = dict[s[0]]
# for i in dict:
#     if dict[i] != value:
#         print(False)
# print(True)

frequencies = dict.values()
print(len(set(frequencies)) == 1)


'''
option with counter'''
from collections import Counter
myMap = Counter(s)
frequencies = myMap.values()
print(len(set(frequencies)) == 1)