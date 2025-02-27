'''
By "counting", we are referring to tracking the frequency of things.
'''

'''
Example 1: You are given a string s and an integer k. 
Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".

basically find longest substring with 2 distint carchert 
'''
s = "eceba"
k = 2

left=0
maxlen=0
thisdict={}

for right in range(len(s)):
    thisdict[s[right]] += 1
    if len(thisdict) == 2:
        maxlen = max(maxlen, right - left + 1)
    while len(thisdict) > 2:
        thisdict[s[left]] -= 1
        if thisdict[s[left]] <= 0:
            del thisdict[s[left]]
        left += 1
print(maxlen)
