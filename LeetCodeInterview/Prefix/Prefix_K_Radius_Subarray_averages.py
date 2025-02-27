""" K Radius Subarray Averages """
'''
You are given a 0-indexed array nums of n integers, and an integer k.
The k-radius average for a subarray of nums centered at some index i with 
the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). 
If there are less than k elements before or after the index i, then the k-radius average is -1.
Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
The average of x elements is the sum of the x elements divided by x, using integer division. 
The integer division truncates toward zero, which means losing its fractional part.
For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
'''
nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
k = 3

prefix = [nums[0]]

"now the prefix will have the sum "
for i in range(1, len(nums)):
    prefix.append(nums[i] + prefix[-1])


''' need to find teh queries for when k i valid '''
''' queries = [[0, 3], [2, 5], [2, 4]]'''

# queries=[]
# for i in range(k, len(nums)):
#     if k+i < len(nums):
#         queries.append([i-k,i+k])


ans = [-1] * len(nums)
# for x, y in queries:
#     curr = prefix[y] - prefix[x] + nums[x]
#     average = curr // (k*2+1)
#     ans[x+k]=average
# print(ans)

for i in range(k, len(nums) - k):
    leftBound, rightBound = i - k, i + k
    subArraySum = prefix[rightBound] - prefix[leftBound] + nums[leftBound]
    average = subArraySum // (2 * k + 1)
    ans[i] = average
    #  subArraySum = prefix[rightBound + 1] - prefix[leftBound]
    #  average = subArraySum // (2 * k + 1)
    #   ans[i] = average

print (ans)

''' now lets improve it?'''
nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
k = 3
   # When a single element is considered then its averafge will be the number itself only.
if k == 0:
     print( nums)

window_size = 2 * k + 1
n = len(nums)
averages = [-1] * n

    # Any index will not have 'k' elements in it's left and right.
if window_size > n:
    print ( averages)

    # Generate 'prefix' array for 'nums'.
    # 'prefix[i + 1]' will be sum of all elements of 'nums' from index '0' to 'i'.
prefix = [nums[0]]
for i in range(1, n):
    prefix[i] = nums[i] + prefix[-1]

    # We iterate only on those indices which have atleast 'k' elements in their left and right.
    # i.e. indices from 'k' to 'n - k'
for i in range(k, n - k):
    leftBound, rightBound = i - k, i + k
    subArraySum = prefix[rightBound+1] - prefix[leftBound]
    average = subArraySum // window_size
    averages[i] = average

print ( averages)

''' the my solution effficient '''
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        "now the prefix will have the sum "
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        ''' need to find teh queries for when k i valid '''
        ''' queries = [[0, 3], [2, 5], [2, 4]]'''

        # queries = []
        # for i in range(k, len(nums)):
        #     if k + i < len(nums):
        #         queries.append([i - k, i + k])

        ans = [-1] * len(nums)
        for i in range(k, len(nums) - k):
            leftBound, rightBound = i - k, i + k
            subArraySum = prefix[rightBound] - prefix[leftBound] + nums[leftBound]
            average = subArraySum // (2 * k + 1)
            ans[i] = average
        return (ans)

