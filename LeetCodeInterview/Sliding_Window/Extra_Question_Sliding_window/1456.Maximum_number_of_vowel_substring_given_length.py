'''
1456. Maximum Number of Vowels in a Substring of Given Length
'''

'''
Given a string s and an integer k, return the maximum number of 
vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Input: s = "abciiidef", k = 3
Output: 3
'''

s = "leetcode"
k = 3

s = list(s)
n= len(s)

left=0
right=k

vowels = ["a", "e", "i", "o", "u"]
count= 0
secondcount=0
''' initialised the window first'''
for i in range(k):
    if s[i] in vowels:
        count +=1
''' sliding the window'''
secondcount=count
for right in range(right,len(s)):
    if s[right] in vowels:
        secondcount += 1
    if s[left] in vowels:
        secondcount -= 1
    left +=1
    count= max(count,secondcount)
print(count)
