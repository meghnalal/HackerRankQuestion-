'''Example 1: Given a string s, return true if it is a palindrome, false otherwise.
A string is a palindrome if it reads the same forward as backward.
That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".'''


s="abcdcba"
left= 0
right = len(s)-1

while left < right :
    if s[left] == s[right]:
        left += 1
        right -= 1
    else:
        print(False)
print(True)

''' Function '''

def check_if_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

input_string = "abcdcba"
print(check_if_palindrome(input_string))
