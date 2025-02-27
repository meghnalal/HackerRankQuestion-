'''
Given a string s and an integer k, return the maximum number of vowel
letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
'''

s = "leetcode"
k = 3

s = list(s)
vowels = ["a", "e", "i", "o", "u"]
count=0
for i in range(k):
    if s[i] in vowels:
        count += 1
ans = count

for right in range(k, len(s)):
    if s[right] in vowels:
        count += 1
    if s[right-k] in vowels:
        count -= 1
    ans = max(ans, count)
print(ans)


