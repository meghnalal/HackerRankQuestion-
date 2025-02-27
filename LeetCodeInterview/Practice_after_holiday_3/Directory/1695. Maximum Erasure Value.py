'''
1695. Maximum Erasure Value
'''

'''
You are given an array of positive integers nums and want to erase a 
subarray containing unique elements. 
The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, 
that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
'''
from collections import defaultdict
count= defaultdict(int)
nums = [4,2,4,5,6]
sumarr=0
left= 0
ans=0
for right in range(len(nums)):
    count[nums[right]] += 1
    while count[nums[right]] > 1 :
        sumarr -= nums[left]
        count[nums[left]] -= 1
        if count[nums[left]] == 0:
            del count[nums[left]]
        left += 1
    sumarr += nums[right]
    ans= max(ans,sumarr)
