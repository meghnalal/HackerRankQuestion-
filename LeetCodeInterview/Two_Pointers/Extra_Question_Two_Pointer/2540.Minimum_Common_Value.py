"""
2540. Minimum Common Value
"""

'''
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
return the minimum integer common to both arrays. If there is no common 
integer amongst nums1 and nums2, return -1.
Note that an integer is said to be common to nums1 and nums2 if 
both arrays have at least one occurrence of that integer.

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
'''

nums1 = [1,2,3,6]
nums2 = [0,3,4,5]
i , j = 0 , 0

current_min = -1
while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
        current_min = nums1[i]
    if nums1[i] < nums2[j]:
        i += 1
    else:
        j += 1
print(current_min)
