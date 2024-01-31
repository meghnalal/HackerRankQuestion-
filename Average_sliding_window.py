'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
'''


nums = [1,12,-5,-6,50,3]
k= 4
res = float('-inf')
initial=0
j=0

for i in range(len(nums)):

    initial += nums[i]
    if i-j == k-1  :
        res= max(res, initial)
        initial -= nums[j]
        j += 1

print(res/k)


nums = [1,12,-5,-6,50,3]
k= 4
res = float('-inf')
initial=0
j=0
i=0

while i < len(nums):

    initial += nums[i]
    if i-j == k-1 :
        res= max(res, initial)
        initial -= nums[j]
        j += 1
    i += 1
print(res/k)

''' variable array  find biggest array that sum to  5  - invented problem works great '''

nums = [1, -2, 3, 4, -1, 2, 1, -5, 4]
k = 6
i=0
j=0
sum_start =0
lenarray= 0

while i < len(nums):
    sum_start += nums[i]
    if sum_start == k:
        lenarray = max(lenarray,i-j +1)


    if sum_start > k:
        sum_start -= nums[j]
        j += 1

    i += 1

print(lenarray)

''' 
2760. Longest Even Odd Subarray With Threshold

longest subarray that satisfy the following condition 

For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2
For all indices i in the range [l, r], nums[i] <= threshold

Input: nums = [3,2,5,4], threshold = 5
Output: 3
Explanation: In this example, we can select the subarray that starts at l = 1 and ends at r = 3 => [2,5,4]. This subarray satisfies the conditions.
Hence, the answer is the length of the subarray, 3. We can show that 3 is the maximum possible achievable length.



'''

nums= [3,2,5,4]
threshold = 5
r=0
ans=0
for i in range(len(nums)):

    if nums[i] % 2  == 0 and nums[i] <= threshold:
        r = i + 1

        while r < len(nums) and nums[r] % 2 != nums[r-1]%2 and  nums[r] <= threshold:

          r += 1

        ans = max(ans, r - i)
    print(ans)


'''max subarray with sum 6'''

nums = [1, -2, 3, 4, -1, 2, 1, -5, 4]
k = 6
i=0
j=0
sum_start =0
lenarray= 0


while i < len(nums):
    sum_start += nums[i]

    if sum_start == k :
        lenarray = max(lenarray, i-j+1 )

    if sum_start > k :
        sum_start -= nums[j]
        j += 1
    i +=1
print(lenarray)

'''

Given an integer array and a positive integer `k`, find the minimum sum contiguous subarray of size `k`.

Input : nums[] = [10, 4, 2, 5, 6, 3, 8, 1], k = 3
Output: [4, 2, 5]

Input : nums[] = [1, 4, 5, 3, 8], k = 6
Output: [1, 4, 5, 3, 8]

Note: Since an input can contain several minimum sum subarrays of size `k`, the solution can return any one of them.

'''

nums = [10, 4, 2, 5, 6, 3, 8, 1]
k = 3
i=0
j=0
min_sum= float('+inf')
current_sum= 0
min_sum_array=[]
if k >= len(nums):
    print(sum(nums))
while i < len(nums):
    current_sum += nums[i]
    if i - j +1 == k:
        if current_sum< min_sum:
            min_sum = min(min_sum,current_sum)
            min_sum_array = nums[j:i+1]
        current_sum -= nums[j]
        j +=1
    i +=1
print(min_sum_array)