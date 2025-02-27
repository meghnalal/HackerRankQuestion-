'''
Example 1: Given a string s, return true if it is a palindrome, false otherwise.

A string is a palindrome if it reads the same forward as backward. That means,

after reversing it, it is still the same string. For example: "abcdcba", or "racecar".

'''

'Its better with function due to return '

s = 'abcdca'

left = 0
right = len(s)-1

while left < right :
    if s[left] != s[right]:
        print(False)
        break
    left += 1
    right -= 1
print(True)

'''
Example 2: Given a sorted array of unique integers and a target integer, return true if ' 
'there exists a pair of numbers that sum to target, false otherwise. This problem is similar ' 
'to Two Sum. (In Two Sum, the input is not sorted).
For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.'''

nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13

left = 0
right = len(nums)-1

while left < right:
    if nums[left] + nums[right] == target:
        print(True)
    if nums[left] + nums[right] > target:
        right -= 1
    else:
        left += 1
