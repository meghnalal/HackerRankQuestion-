'''
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

'''

' i dont need to square i just need to make positive '
nums = [-4, -1, 0, 3, 10]
ans = [0] * len(nums)
i = 0
j = len(nums) - 1

for x in range(len(nums) - 1, -1, -1):
    if abs(nums[i]) < abs(nums[j]):
        ans[x] = abs(nums[j])
        j -= 1
    else:
        ans[x] = abs(nums[i])
        i += 1
print(ans)
