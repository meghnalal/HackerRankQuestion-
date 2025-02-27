'''

'''

'''
Given a 2D array nums that contains n arrays of distinct integers, 
return a sorted array containing all the numbers that appear in all n arrays.

For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.
'''
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]

thisdict= {}
left = 0
n= len(nums)
keys_with_value_3=[]
for i in nums:
    for j in i:
        if j in thisdict:
            thisdict[j] += 1
            if thisdict[j] == n:

        else:
            thisdict[j] = 1

# keys_with_value_3 = [key for key, value in thisdict.items() if value == 3]
keys_with_value_3=[]
for key, value in thisdict.items():
    if value ==3:
        keys_with_value_3.append(key)
print(sorted(keys_with_value_3))