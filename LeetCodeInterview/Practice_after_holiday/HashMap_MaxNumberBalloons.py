'''

Maximum Number of Balloons

'''

'''Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.'''

text = "leetcode"

from collections import defaultdict

balloon= 'balloon'
counts = defaultdict(int)
countstext = defaultdict(int)
ans = float("inf")
for i in balloon:
    counts[i] += 1

for j in text:
    if j in counts:
        countstext[j] += 1

for x in counts:
   ans= min(ans,countstext[x] // counts[x])
print(ans)