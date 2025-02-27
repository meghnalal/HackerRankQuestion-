'''
example2
'''

'''
Example 2: You are given a binary string s (a string containing only "0" and "1"). 
You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.
'''
s = "1101100111"
k = 1
left = 0
count = 0
ans=0
for right in range(len(s)):
    if s[right] == '0':
       count += 1
    while count > k :
        if s[left] == '0':
            count -= 1
        left += 1
    ans= max(ans, right- left +1)

print(ans)
