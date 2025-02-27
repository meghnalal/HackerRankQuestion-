'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''


s = ["h","e","l","l","o"]

left = 0
right = len(s)-1
temp= ''
def reverse_string(s):
    left = 0
    right = len(s) - 1
    while left < right:
        # temp= s[left]
        # s[left] = s[right]
        # s[right] = temp
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return (s)


''' s.reverse is more efficient '''