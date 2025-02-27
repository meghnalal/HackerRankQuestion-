'''

Given an array of positive integers nums and an integer k,
return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100,
the answer is 8. The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6 ]
'''

nums = [10, 5, 2, 6]

k = 100

left= 0

product=1
validarray=0
if k <= 1:
    print (0)
for right in range(len(nums)):
    product *= nums[right]

    while product >= k:
        product //= nums[left]
        left +=1

    validarray = validarray + (right-left +1)
print(validarray)


