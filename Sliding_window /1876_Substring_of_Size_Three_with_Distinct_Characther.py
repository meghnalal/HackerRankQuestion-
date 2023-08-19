"""
1876- LeetCode
Substrings of Size Three with Distinct Characters

A string is good if there are no repeated characters.

Given a string s, return the number of good substrings of length three in s.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

Example:
      Input= "xyzzaz"
      Output = 1
      Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
                   The only good substring of length 3 is "xyz"
"""
''' solution where i defined the window and used sets '''

x = "xyzzaz"
k = 3

''' initial window '''
window = x[:k]
unique = len(set(window))

count = 0
if unique == k :
    count += 1
''' looping through the other windows'''
for i in range(len(x)-k):
    window = x[i+1:i+k+1]
    next_unique = len(set(window))
    if next_unique == k:
        count += 1
print(count)

''' solution with pointers and avoids sets its a better solution overall '''
x = "xyzzaz"
k = 3
i = 0
j = 0
count = 0
while j < len(x):
    if j-i+1 < k :
        j += 1
    if j-i+1 == k:
        if x[i] != x[i+1] and x[i+1] != x[i+2] and x[i+2] != x[i]:
            count += 1
        i += 1
        j += 1
print(count)