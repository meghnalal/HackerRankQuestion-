'''

268. Missing Number

'''
'''

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

'''

nums = [0,1]
setnums = set(nums)

for i in range(len(nums)+1):
    if i not in setnums:
        print(i)