'''
Given an array of integers nums and an integer target,
return indices of two numbers such that they add up to target. You cannot use the same index twice.
'''

nums = [2,7,11,15]
target = 9
dict={}
val=0
for i in range(len(nums)):
    num = nums[i]
    val = target-num
    if val in dict:
        print[i,dict[val]]
    dict[num] = i
print(dict)
