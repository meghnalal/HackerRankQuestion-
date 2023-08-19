array_length = 3
array_working = [1,2,3,5,4,2,6]
target = 12

'''
1- need to do sum of the first  element 
2- move to the next indices and add the 4 and remove the 1 
3- if found still continue till end of array 
'''
'''
for the sum there is 2 method there is :
1- slicing  --> sum(array_working[0:3])
2- for loop -->
sum_three_elements = 0
for i in range(array_length):
    sum_three_elements += array_working[i]
'''

sum_array = sum(array_working[:array_length]) # first one will be 6
subarray = []
if sum_array == target:
    subarray = array_working[:array_length]

for i in range(len(array_working)-array_length):
    sum_array = sum_array - array_working[i] + array_working[i+array_length]
    if sum_array == target:
        subarray = subarray + [array_working[i+1:i+array_length+1]] # because i wanted to print subarray you can simply add without having it as an array
print(subarray)

'''
lesson learnt that it did the sum of the first 3 
pick the right indices for the subarray 
splitting array in python 
reminder this example constant array not dynamic 
'''

'''
A string is good if there are no repeated characters.

Given a string s, return the number of good substrings of length three in s.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

s = 'xyzzaz'
substring = [xyz] [yzz] [zza] [zaz] 
output should be 1 as the only one is xyz 
'''

length_subarr = 3
s = 'xyzzazdf'

sub = s[:length_subarr]
length_of_sum =  set(sub)

count =0
if len(length_of_sum) == 3:
    count += 1

for i in range(len(s)-length_subarr):
    sub = s[i+1:i+length_subarr+1]
    length_of_sum = set(sub)
    if len(length_of_sum) == 3:
        count += 1
print(count)


'''Beats 34.11%of users with Python3 leetcode accepted '''

''''
Question : Finding k-Beauty of a number 

you have integer num like num=240 
and k is 2 
is 24 divisor of 240 --> Yes
is 40 divisor of 240 --> Yes
Output should be 2
'''

num = 240
k = 2
str_num = str(num)

if k > num:
    print('not valid')
num_div = str_num[:k]
count = 0
if int(num_div) != 0 and num % int(num_div) == 0:
    count += 1
for i in range(len(str_num)-k) :
    num_div= str_num[i+1:i+k+1]

    if int(num_div) != 0 and num % int(num_div) == 0:
        count +=1
print(count)

'''
2379- Minimum recolors to get K consecutive Black Blocks 

Basically you get given a string of blcoks='WBBWWBBWBW'
You can convert the white to be black 
however you need to find the least amount for that 
for a given k of consecutive occurances

blcoks='WBBWWBBWBW'
k=7 
Output =3

1 ---> check how many conversion takes for the first 7 
2 ---> sliding window to the next one and count up
3 ---> compare with previous count and only update if its < then the one before 
'''

block = 'WBBWWBBWBW'
K = 7

block_seven = block[:K]
count = 0

count = block_seven.count('W')

for i in range(len(block)-K):
    block_seven = block[i+1:i+K+1]
    count_new = block_seven.count('W')
    count = min(count, count_new)
print(count)

''' potential issue here is that i am using .count in teh for loop adds to time complexity '''


''' best solution here below beats all the other solutions '''
block = 'WBWBBBW'
K = 2

block_seven = block[:K]


count= block_seven.count('W')

min_count=count

for i in range(K,len(block)):
    if block[i] == 'W':
        count += 1
    if block[i -K] == 'W':
        count -= 1
    if count < min_count:
        min_count = count
print(min_count)

''' you  can also do with the method by adding so start at  0 and check 0+7 then 1 and checks 1+7 '''
block = 'WBWBBBW'
K = 2

block_seven = block[:K]


count= block_seven.count('W')

min_count=count

for i in range(len(block)-K):
    if block[i] == 'W':
        count -= 1
    if block[i +K] == 'W':
        count += 1
    if count < min_count:
        min_count = count
print(min_count)

'''
Minimum differce between Highest and Lowest K Score 
you get given a list nums =[]
you also get given a integer k which represents k students 

this one i smore tricky because i need to look at the minus 

does it matter if its consecutive?
'''

nums =[9,4,1,7]
sorted_list = sorted(nums, reverse=True)
k=2
initial_diff=0
if len(nums) == 1:
    print (initial_diff)

initial_diff = float('inf')

'''
first initial difference will be 9-7 = 2

absolute_diff |2-9|| = 7 took away the initial value  so this is going to be 
starting at 0 then 1 and so on (in the loop)
second diff will take teh absolute - the next value 
second value what we check as initial difference   
'''
for i in range(len(sorted_list)-k+1):

    second_diff= sorted_list[i]- sorted_list[i+k-1]

    if second_diff < initial_diff:
        initial_diff = second_diff

print (initial_diff)

''' 
this solution is with the pointer method 
this solution similar to  the other one and 
it takes to the same conclusion ish 
'''

nums =[9,4,1,7]
nums.sort()
k=3

l, r = 0, k-1
res = float('inf')
while r < len(nums):
    res = min(res, nums[r] - nums[l])
    l, r = l+1, r+1
print(res)

'''
643. Maximum Average Subarray I

this solution work just important thing not to nest sum inside the loop 
'''

nums = [1,12,-5,-6,50,3]
k = 4

initial_sum = sum(nums[:k])
initial_average = initial_sum /k
for i in range(len(nums)-k):
    initial_sum = (initial_sum - nums[i] + nums[i+k])
    average = initial_sum / k
    if average > initial_average:
        initial_average = average
print(initial_average)

'''
pointer method
'''
nums = [1,12,-5,-6,50,3]
k = 4
l = 0
r = k

initial_sum = sum(nums[:k])
initial_average = initial_sum /k
while r < len(nums):
    initial_sum = initial_sum - nums[l] + nums[r]
    average = initial_sum / k
    if average > initial_average:
        initial_average = average
    l += 1
    r += 1
print(initial_average)

'''best solution'''
nums = [1,12,-5,-6,50,3]
k = 4

initial_sum = sum(nums[:k])
ans = initial_sum
for i in range(len(nums)-k):
    initial_sum = (initial_sum - nums[i] + nums[i+k])
    if initial_sum > ans:
        initial_average = ans
print(initial_sum/k)