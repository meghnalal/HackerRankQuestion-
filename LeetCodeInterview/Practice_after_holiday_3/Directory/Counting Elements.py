'''
Counting Elements
'''
'''
Given an integer array arr, count how many elements x there are, 
such that x + 1 is also in arr. If there are duplicates in arr, count them separately.
'''

arr = [1,1,3,3,5,5,7,7]
setarr= set(arr)
count=0
for i in arr:
    if (i + 1) in setarr:
        count +=1

