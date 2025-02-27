''' 2351. First Letter to Appear Twice'''

'''
Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.

Input: s = "abccbaacz"
Output: "c"
'''

s = "abccbaacz"

dict = {}
count=0
for i in range(len(s)):
    letter = s[i]
    if letter in dict:
        print(letter)
    dict[letter]=i


''' better efficient way'''
seen = set()
for c in s:
    if c in seen:
        print(c)
    seen.add(c)