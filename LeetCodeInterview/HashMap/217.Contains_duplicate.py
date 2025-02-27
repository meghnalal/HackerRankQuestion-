'''
217. Contains Duplicate
'''
''' checking for existance'''
'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
Input: nums = [1,2,3,1]
Output: true
Input: nums = [1,2,3,4]
Output: false
'''

nums = [1,2,3,1]
n= len(nums)

setnumlen= len(set(nums))

if n == setnumlen:
    print(False)
else:print(True)


''' coding '''


def containsDuplicate(self, nums: List[int]) -> bool:
    n = len(nums)
    setnumlen = len(set(nums))
    return (n != setnumlen)