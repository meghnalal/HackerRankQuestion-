
'''Brute Force solution very slow runtime 426ms'''
nums=[8,1,2,2,3]
result = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if i != j and nums[i] > nums[j]:
            count += 1
    result.append(count)
print(result)


'''he idea is to use the merge sort algorithm to sort the input array 
and keep track of the original indices of the elements. Then, for each 
element in the sorted array, we can count the number of elements that 
are smaller than it by looking '''


nums=[8,1,2,2,2]

'''what if i use the index and sort it and return the index '''
count = {}
'''this calculates frequency '''
for num in nums:

    count[num] = count.get(num, 0) + 1
print(count)
'''sort the first value {key:}'''
sorted_nums = sorted(count.keys())

'''makes leng of array [0 0 0 0 0]'''
prefix_sum = [0] * len(sorted_nums)

''' basically takes the first index 1 = prefix[0]+ count[sorted_num[0]]= 0+1 
which is the count of the index value 0 of sorted num'''
for i in range(1, len(sorted_nums)):
    print(i)
    prefix_sum[i] = prefix_sum[i - 1] + count[sorted_nums[i - 1]]
print(prefix_sum)

result = []
for num in nums:
    result.append(prefix_sum[sorted_nums.index(num)])

print(result)

''' wonder if there is a easier soluton '''





