"""
Length of longest subarray of sum less than or equal to k

"""

'''
'''

nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8

l=0
r=0
sumval=0
ans = 0

while r < len(nums):

    if sumval<=k:
        r += 1
        sumval = sum(nums[l:r])

    if sum(nums[l:r])>k:
        sumval -= nums[l]
        l += 1
    ans = max(ans, r - l )
print(ans)



''' with for loop '''

nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8

l=0
r=0
sumval=0
ans = 0
for r in range(len(nums)):
    sumval += nums[r]
    while sumval>k:
            sumval -= nums[l]
            l += 1
    ans = max(ans, r - l+1)
print(ans)



'''
Example 2: You are given a binary string s (a string containing only "0" and "1"). 
You may choose up to one "0" and flip it to a "1". 
What is the length of the longest substring achievable that contains only "1"?
For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, 
the string becomes 1111100111.
'''

s = "1101100111"

l=0
r=0
curr=0
ans=0

for r in range(len(s)):
    if s[r] == "0":
        curr +=1

    while curr > 1:
        if s[l] == "0":
            curr -= 1
        l += 1
    ans = max(ans, r - l+1)
print(ans)
