'''
1695. Maximum Erasure Value
'''

'''
You are given an array of positive integers nums and want to erase a subarray containing unique elements. 
The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, 
that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
'''
from collections import defaultdict
nums = [5,2,1,2,5,2,1,2,5]
maxdict=defaultdict(int)
sum=0
sum1= 0
left=0
for right in range(len(nums)):
    maxdict[nums[right]] += 1
    sum1 += nums[right]
    while maxdict[nums[right]] > 1:
        sum1 -= nums[left]
        maxdict[nums[left]] -= 1
        if nums[left] == 0 :
            del nums[left]
        left += 1
    sum = max(sum, sum1)

print(sum)

