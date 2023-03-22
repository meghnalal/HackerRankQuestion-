nums = [3,2,4]
target = 6
def twoSum(nums, target):
    result = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
    return result

nums = [3,2,4]
target = 6

print(twoSum(nums,target))

'''how to make it more efficient ad that has 02 time complexity '''

def twoSum(nums, target):
    visited = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in visited:
            return [visited[diff], i]
        visited[num] = i
    return []

nums = [3, 2, 4, 3, 4]
target = 6

print(twoSum(nums, target))