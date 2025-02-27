'''

'''

'''
Example 3: 1941. Check if All Characters Have Equal Number of Occurrences

Given a string s, determine if all characters have the same frequency.

For example, given s = "abacbc", return true. All characters appear twice. 
Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
'''

s = "abacbc"

thisdic= {}

for i in s:
    if i in thisdic:
        thisdic[i] += 1
    else:
        thisdic[i] = 1
# thisdic = defaultdict(int)
#         for c in s:
#             thisdic[c] += 1
frequencies = thisdic.values()
print(len(set(frequencies)) == 1 )

''' better way of doing this '''
from collections import Counter
s = "abacbc"
len(set(Counter(s).values())) == 1