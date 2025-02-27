'''Example 2: Given a sorted array of unique integers and a target integer,
return true if there exists a pair of numbers that sum to target, false otherwise.
This problem is similar to Two Sum. (In Two Sum, the input is not sorted).
For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.'''

nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13

left= 0
right= len(nums) -1
cursum=0

while left < right:
    cursum = nums[left] + nums[right]
    if cursum == target:
        print(True)
        break
    if cursum > target:
        right -= 1
    else:
        left +=1
else:
    print(False)

def target_sum(nums,target):
    left = 0
    right = len(nums) - 1
    while left < right:
        cursum = nums[left] + nums[right]
        if cursum == target:
            return True
        if cursum > target:
            right -= 1
        else :
            left += 1
    return False

nums = [1, 2, 5, 6, 8, 9, 14, 15]
target = 13

print(target_sum(nums,target))