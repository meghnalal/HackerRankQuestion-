'''
A string is good if there are no repeated characters.

Given a string s, return the number of good substrings of length three in s.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
The only good substring of length 3 is "xyz".
'''
s = "xyzzaz"
k = 3
count= 0
i=0
j=0
while j < len(s):
    if j-i+1 < k:
        j += 1
    if j-i+1 == k:
        if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i+2] != s[i]:
            count +=1
        i += 1
        j += 1
print( count)

'''You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average 
value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
'''
nums = [1,12,-5,-6,50,3]
k = 4
j= 0
i= 0
max_sum= 0
while j < len(nums):
    if len(nums[i:j]) < k:
        j += 1
    if len(nums[i:j]) == k:
        addition = sum(nums[i:j])
        if addition > max_sum:
            max_sum = addition
        j +=1
        i +=1
print (addition/k)







