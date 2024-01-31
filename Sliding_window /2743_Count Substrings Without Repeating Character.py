"""
You are given a string s consisting only of lowercase English letters.
We call a substring special if it contains no character which has occurred
at least twice (in other words, it does not contain a repeating character).
Your task is to count the number of special substrings.
For example, in the string "pop", the substring "po" is a special
substring, however, "pop" is not special (since 'p' has occurred twice).

Input: s = "abcd"
Output: 10
Explanation: Since each character occurs once, every substring is a special substring.
We have 4 substrings of length one, 3 of length two, 2 of length three,
and 1 substring of length four. So overall there are 4 + 3 + 2 + 1 = 10 special substrings.
"""
from collections import Counter

s = "abcd"
ans= 0
l=0
cnt = Counter()
ans = j = 0
for i, c in enumerate(s):
    cnt[c] += 1
    while cnt[c] > 1:
            cnt[s[j]] -= 1
            j += 1
    ans += i - j + 1
print(ans)