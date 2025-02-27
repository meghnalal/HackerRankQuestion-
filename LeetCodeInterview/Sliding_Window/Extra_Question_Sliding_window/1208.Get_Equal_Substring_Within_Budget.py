'''
1208. Get Equal Substrings Within Budget
'''

'''
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| 
(i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring 
of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed 
to its corresponding substring from t, return 0.


Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.
 abs(ord('a')- ord('b'))
'''

s = "abcd"
t = "acde"
maxCost = 0

left=0
maxlen_array=0
count=0

for right in range(len(s)):
    count= count + abs(ord(s[right])- ord(t[right]))
    while count > maxCost:
        count = count - abs(ord(s[left])- ord(t[left]))
        left +=1
    maxlen_array= max(maxlen_array,right-left+1)
print(maxlen_array)