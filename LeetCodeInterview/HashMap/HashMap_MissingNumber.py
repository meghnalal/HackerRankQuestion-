'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

nums = [9,6,4,2,3,5,7,0,1]
z=set(nums)
n= len(nums)
for i in range(n+1):
    if i not in z:
        print(i)

''' ok issue with max value if ist at the end what i can do as well is reverse for loop'''

setnums= set(nums)
n=len(nums)
for i in range(n, -1, -1):
    if i not in setnums:
        print(i)

''' both work'''