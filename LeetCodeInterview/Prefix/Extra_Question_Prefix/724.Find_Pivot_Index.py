'''
724. Find Pivot Index
'''

'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the 
left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are 
no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

'''

nums = [1,7,3,6,5,6]

sum_left=[0]

max_altitude=0

for i in range(0,len(nums)):
    sum_left.append(nums[i]+sum_left[-1])
print(sum_left)
''' n needs to be here after prefix array'''
n=len(sum_left)-1
index=-1
for j in range(len(sum_left)-1):
    sum_left1=sum_left[j]
    sum_right = sum_left[n] - sum_left[j+1]
    if sum_left[j] == sum_right:
        index = j
        break
print(index)

