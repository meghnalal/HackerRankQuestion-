'''
Max Sum of a Pair With Equal Sum of Digits
'''

'''
You are given a 0-indexed array nums consisting of positive integers. 
You can choose two indices i and j, such that i != j, and the sum of digits 
of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all 
possible indices i and j that satisfy the conditions.

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
'''
from collections import defaultdict

nums = [279,169,463,252,94,455,423,315,288,64,494,337,409,283,283,477,248,8,89,166,188,186,128]

storing= defaultdict(int)

def digit_sum(n):
    num_str = str(n)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    return sum

# for i in nums:
#     storing[digit_sum(i)].append(i)
ans = 0

# for key in storing:
#     if len(storing[key]) == 2:
#         ans = max(ans,sum(storing[key]))
#     if len(storing[key]) > 2:
#         storing[key].sort()
#         tmp = storing[key]
#         pair_sum= sum(tmp[-2:])
#         ans = max(ans, pair_sum)
#
# print( -1 if ans == 0 else ans)

for i in nums:
    sumdigit= digit_sum(i)
    if sumdigit in storing:
        ans = max(ans, i + storing[sumdigit])
    storing[sumdigit] = max(storing[sumdigit], i)

print( -1 if ans == 0 else ans)
