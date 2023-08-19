from typing import List

# Write any import statements here
# Row N of seats
# K empty seats left and right
# M diner sat at the table
# Maximum number of diner who can sit at the table

'''
example so if 
n=10 number of seats
k = 1 distance between left and right 
m=2 people who are sat 
s= [2,6] index of where they are sat  
how many people can sit 


'''

'''
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here


    return 0
'''
'''iterate of array of 10 '''
n = 10
k = 1
m = 2
s = [ 2 , 6]
seatcantbeused=[]
emptyseatright=[]
for i in s:
    seatcantbeused.append(i-k)
    seatcantbeused.append(i+k)
s= s + seatcantbeused
sorted_list = sorted(s)
count = 0
for i in range(len(sorted_list)-1):
    if sorted_list[i] + 1 != sorted_list[i+1] :
        count = count+1
    elif (i ==  len(sorted_list)-1) and len(sorted_list-1)< n:
        count = count+1
print(count)
print(sorted_list)

indices = []
for i in range(s[0], ):
    indices.append(i)
print( indices)

