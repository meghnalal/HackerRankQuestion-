'''
303. Range Sum Query - Immutable
'''

'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

'''
''' logic that i converted in function '''
array=[-2, 0, 3, -5, 2, -1]
left=0
right=2

prefix=[array[0]]

for i in range(1,len(array)):
    prefix.append(array[i]+prefix[-1])
print(prefix)
summing= prefix[right]-prefix[left]+array[left]
print(summing)


class NumArray:

    def __init__(self, nums:[int]):
        self.nums = nums
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        self.prefix= prefix

    def sumRange(self, left: int, right: int) -> int:
        summing = self.prefix[right] - self.prefix[left] + self.nums[left]
        return(summing)
nums=[-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
left=0
right=5
param_1 = obj.sumRange(left,right)
print(param_1)