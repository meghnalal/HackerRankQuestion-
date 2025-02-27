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
counting = defaultdict(int)
left=0
ans= 0
currans=0

for right in range(len(nums)):
    counting[nums[right]] += 1
    while counting[nums[right]] > 1 :
        counting[nums[left]] -= 1
        currans -= nums[left]
        left +=1
    currans += nums[right]
    ans= max(ans,currans)





