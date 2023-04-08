my_list = [1, 2, 1, 3,3]
indices_of_values = {}
index_val=[]
'''Brute Force Solution on2'''
for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i] == my_list[j] and i<j :
            index_val.append((i,j))
print(len(index_val))

'''Actual solution'''
nums = [1, 2, 1, 3,3]
count = []
for num in nums:
    if len(count) <= num:
        count += [0] * (num - len(count) + 1)
        count[num] += 1
        totalCount = 0
for i in count:
        totalCount += ((i) * (i-1)) // 2
print(totalCount)



'''Appending to a list can take more runtime than initializing a list with the multiplication 
operator when the list needs to be resized multiple times. When you append an element to a list, 
Python needs to check whether the list has enough capacity to store the new element. If the list 
doesn't have enough capacity, Python needs to allocate a new (larger) array, copy the existing 
elements over to the new array, and then append the new element to the new array. This process 
can take more time than simply initializing a list with the correct size upfront using the 
multiplication operator.'''

'''Better Solution'''
max_value = max(nums)
count = [0] * (max_value + 1)
for num in nums:
    count[num] += 1
    totalCount = 0
for i in count:
    totalCount += ((i) * (i-1)) // 2
print( totalCount)

'''Best Runtime'''

count = [0] * 102
for num in nums:
    count[num] += 1
    totalCount = 0
for i in count:
    totalCount += ((i) * (i-1)) // 2
print( totalCount)


def numIdenticalPairs(nums):

    # Calculate the frequency of each number
    count = [0] * 102

    for num in nums:
        count[num] += 1

    totalCount = 0

    # Caclulate total number of pairs possible
    for i in count:
        totalCount += ((i) * (i-1)) // 2

    return totalCount