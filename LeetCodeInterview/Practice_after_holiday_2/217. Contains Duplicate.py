'''
217. Contains Duplicate
'''

'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
'''

nums = [1,2,3,4]
# this process the whole dataset in set
print(len(set(nums)) != len(nums))

seen = set()
for num in nums:
    if num in seen:
        print(True)
    seen.add(num)