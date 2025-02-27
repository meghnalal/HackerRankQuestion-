'''
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
'''

nums = [-4, -1, 0, 3, 10]

left =0
right = len(nums)-1
ans= [0] * len(nums)
for i in range(len(nums) - 1, -1, -1):
    if nums[right] ** 2 > nums [left] ** 2:
        ans[i]= nums[right] ** 2
        right -= 1
    else:
        ans[i]= nums[left] ** 2
        left +=1
print(ans)


''' trying it again  '''

nums = [-4, -1, 0, 3, 10]

left = 0
right = len(nums)-1
ans= [0] * len(nums)
for i in range(len(nums)-1, -1, -1):
    if abs(nums[right]) > abs(nums[left]):
        ans[i] = nums[right] ** 2
        right -= 1
    else:
        ans[i] = nums[left] ** 2
        left += 1
print(ans)

''' actual method in term of efficiency '''

A = [-4, -1, 0, 3, 10]
def sortedSquares( A ):
    return sorted(x*x for x in A )

print(sortedSquares(A))