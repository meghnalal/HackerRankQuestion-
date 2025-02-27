'''

'''
'''

'''
from collections import defaultdict

count = defaultdict(int)
nums =[5,5,5,5,5,5,5]
k = 4
left=0

ans= 0
for right in range(len(nums)):
    count[nums[right]] += 1
    while count[nums[right]] > k :
        if count[nums[left]] == 0:
            del count[nums[left]]
        else :
            count[nums[left]] -= 1
        left +=1
    ans= max(ans,right-left +1)
print(ans)