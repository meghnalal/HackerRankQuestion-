'''

303. Range Sum Query - Immutable

'''

'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums 
between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

sumRange(left,right)=prefix[right+1]−prefix[left]
'''


class NumArray:

    def __init__(self, nums:[int]):
        self.nums= nums
        prefix= [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        self.prefix= prefix

    def sumRange(self, left: int, right: int) -> int:
        summing = self.prefix[right] - self.prefix[left] + self.nums[left]
        return(summing)

nums = [-2, 0, 3, -5, 2, -1]  # Example input array
obj = NumArray(nums)

result = obj.sumRange(1, 3)  # Computes sum of nums[1] to nums[3]
print(result)

# nums = [-2, 0, 3, -5, 2, -1]
#
# prefix = [nums[0]]
# for i in range(1,len(nums)):
#     prefix.append(nums[i] + prefix[-1])
#
# sumRange = [[0, 2], [2, 5], [0, 5]]
# for l, r in sumRange:
#     print(l,r)
#     summing= prefix[r] - prefix[l] + nums[l]
#     print(summing)