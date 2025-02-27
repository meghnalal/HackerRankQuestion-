'''

Counting Elements
'''


'''
Input: arr = [1,1,3,3,5,5,7,7]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
'''

arr = [1,1,2,2,5,5,7,7]

# dict={}
# count = 0
# for i in range(len(arr)):
#     num = arr[i]
#     dict[num]= i
arrset= set(arr)
count=0
for i in range(len(arr)):
    if arr[i]+1 in arrset:
       count +=1
print(count)
