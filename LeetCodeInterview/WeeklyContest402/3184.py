'''
3184. Count Pairs That Form a Complete Day I
'''

'''
Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, 
j where i < j and hours[i] + hours[j] forms a complete day.

A complete day is defined as a time duration that is an exact multiple of 24 hours.

For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.


'''

hours = [72,48,24,3]
ans=0
for i in range(len(hours)):
    for j in range(i+1,len(hours)):
        if (hours[i] + hours[j]) % 24 == 0:
            ans += 1

print(ans)

from collections import defaultdict

nums = [12,12,30,24,24]
target = 24
checkpair = defaultdict(int)
ansx=0

''' puting position as value as that is what i need to return --- remeber also you can search keys but not value '''
for i in range(len(nums)):
    num=nums[i]
    rem = num % 24
    complement = (24 - rem) % 24
    if complement in checkpair:
        ansx += checkpair[complement]
    checkpair[rem] +=  1
