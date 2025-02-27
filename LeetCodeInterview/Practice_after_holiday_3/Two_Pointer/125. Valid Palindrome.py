'''
125. Valid Palindrome
'''

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''
s = 'abcdcba'
def check_if_palindrome(s):
    pointer_start = 0
    pointer_end = len(s)-1

    while pointer_start < pointer_end:
        if s[pointer_start] != s[pointer_end]:
            return(False)
        pointer_start += 1
        pointer_end -= 1
    return True

print(check_if_palindrome(s))
