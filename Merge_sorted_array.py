nums1= [1,2,3,0,0,0]
nums2= [2,5,6]
'''lenghts'''
m=3
n=3
'''no need to do thi'''
nums1 = [x for x in nums1 if x != 0]
nums1 = nums1 + nums2
nums1.sort()

'''naive sollution'''

nums1[m:] = nums2

# Sort nums1 in-place
nums1.sort()

# Print the final sorted nums1
print(nums1)

nums1= [1,2,3,0,0,0]
nums2= [0,5,6]

ptr1 = m - 1
ptr2 = n - 1
merged_ptr = m + n - 1

# Merge nums1 and nums2 from the end
while ptr1 >= 0 and ptr2 >= 0:
    if nums1[ptr1] >= nums2[ptr2]:
        nums1[merged_ptr] = nums1[ptr1]
        ptr1 -= 1
    else:
        nums1[merged_ptr] = nums2[ptr2]
        ptr2 -= 1
    merged_ptr -= 1

# Add any remaining elements from nums2 to nums1
#nums1[:ptr2 + 1] = nums2[:ptr2 + 1]

# or this
while ptr2 >= 0:
            nums1[merged_ptr]=nums2[ptr2]
            ptr2 -= 1
            merged_ptr -= 1

# Print the final merged and sorted nums1
print(nums1)

'''pointer method from 0 with creating a new array'''
nums1= [1,2,3]
nums2= [2,5,6]

n=3
m=3
j=0
i=0
k=0

nums3 = [None] * (m + n)

while j < n and i < m:
    if nums1[i] <= nums2[j]:
        nums3[k]=nums1[i]
        i += 1
        k += 1
    else:
        nums3[k] = nums2[j]
        j += 1
        k += 1

while i < m:
        nums3[k] = nums1[i]
        i += 1
        k += 1

while j < n:
        nums3[k] = nums2[j]
        j += 1
        k += 1

print(nums3)