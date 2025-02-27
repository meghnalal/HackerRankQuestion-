''' 917. Reverse Only Letters '''
'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

'''


s = "7_28]"
left = 0
right = len(s)-1
arr =[]

s =list(s)

while left < right:
    while not (s[left]).isalpha() and left < right  :
        left +=1
    while not (s[right]).isalpha() and left < right :
        right -= 1
    else:
        s[left] , s[right] = s[right], s[left]
        left += 1
        right -= 1
print(s)