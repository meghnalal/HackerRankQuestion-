'''

'''

'''
Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.

For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.
'''
nums = [[7,34,45,10,12,27,13],[27,21,45,10,12,13]]

dict={}

for arr in nums:
    for i in arr:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1
print(dict)
n = len(nums)
ans = []
for key in dict:
    if dict[key] == n:
        ans.append(key)
print(ans)
