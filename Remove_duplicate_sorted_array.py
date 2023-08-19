'''issue is  does not modify the array nums even tho solution is correct'''
nums=[1,1,2]

x= []

for i in nums:
    if i not in x:
        x.append(i)
print(len(x))

def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k

removeDuplicates([3,4,4,5,6])

''' 
[3,4,4,5,6]
k=1
4 != 3 k=2
4 != 4 k=2
4 != 5 k=3
5 != 5 k=3
5 != 6 k=4

'''
nums = [1, 1, 1, 2, 2, 3]
k=1
count=1
for i in range(1, len(nums)-1):
    if nums[i] == nums[i-1] and count <= 1:
        nums[k] = nums[i]
        count += 1
        k += 1
    elif nums[i] == nums[i-1] and count > 1:
        nums[k] = nums[i+1]
        k += 1
        count = 1
print (k)



nums = [1, 1, 1, 2, 2, 3]

N=3
C = 'ABA'
string_list = list(C)
for i in range(N):
    if string_list[i] == 'A':
        string_list[i] = 'B'
    else:
        string_list[i] = 'A'
new_string = ''.join(string_list)
print (new_string)


R = 2
C = 3
G = [[0, 0, 1],
     [1, 0, 1]]

def count_ones(matrix):
    count = sum(row.count(1) for row in G)
    probability = count / (C * R)
    return count

# Example usage:
matrix = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

result = count_ones(matrix)
print(result)  # Output: 6
