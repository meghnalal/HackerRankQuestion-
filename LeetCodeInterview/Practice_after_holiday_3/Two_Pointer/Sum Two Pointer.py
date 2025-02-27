'''

'''

'''
Example 2: Given a sorted array of unique integers and a target integer, 
return true if there exists a pair of numbers that sum to target, false otherwise. 
This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
'''

nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13
def check_sum(nums,target):
    p_start = 0
    p_end = len(nums)-1

    while p_start < p_end:
        current_sum = nums[p_start] + nums[p_end]
        if current_sum == target:
            return True
        if current_sum > target :
            p_end -= 1
        else :
            p_start += 1

    return False

print(check_sum(nums, target))