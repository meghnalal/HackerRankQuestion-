"""

Given a binary array nums and an integer k,
return the maximum number of consecutive 1's
in the array if you can flip at most k 0's.

"""
''' the negative way so im adding until we reach k value '''
nums= [1,1,1,0,0,0,1,1,1,1,0]
k = 2


curr_zero=0
countarrray=0
longestarray=0
right=0
left =0
for right in range(len(nums)):
    if nums[right] == 0:
        k -= 1
    while k < 0:
        if nums[left] == 0:
            k += 1
        left += 1
    countarrray = max(right-left+1, countarrray)

print(countarrray)
''' the positive way so im adding until we reach k value '''
nums1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
curr_zero=0
countarrray=0
longestarray=0
right=0
left =0
for right in range(len(nums)):
    if nums[right] == 0:
        curr_zero += 1
    while curr_zero > k:
        if nums[left] == 0:
            curr_zero -= 1
        left += 1
    countarrray = max(right-left+1, countarrray )

print(countarrray)
''' In the function '''
def longestOnes(nums, k):
    left = 0
    max_length = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage:
nums1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k1 = 2
result1 = longestOnes(nums1, k1)
print(result1)  # Output: 6

nums2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k2 = 3
result2 = longestOnes(nums2, k2)
print(result2)  # Output: 10




