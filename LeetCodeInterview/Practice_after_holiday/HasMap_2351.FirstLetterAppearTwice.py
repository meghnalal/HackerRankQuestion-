'''

Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.

'''

s = "abccbaacz"

dict={}

for i in range(len(s)):
    if s[i] in dict:
        print(s[i])
    dict[s[i]]= i
''' BETTER WAY WITH SET AS WE DONT CARE VALUE'''
seen = set()
for c in s:
    if c in seen:
        print(c)
    seen.add(c)