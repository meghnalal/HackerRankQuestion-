'''You are given a 0-indexed two-dimensional integer array nums.

Return the largest prime number that lies on at least one of the
diagonals of nums. In case, no prime is present on any of the diagonals,
return 0.

Note that:

An integer is prime if it is greater than 1 and has no positive integer
divisors other than 1 and itself.
An integer val is on one of thediagonals of nums if there exists an integer
i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1]= val.

In the above diagram, one diagonal is [1,5,9] and another diagonal is [3,5,7].
[[1,2,3],
[5,6,7],
[8,9,10]]
'''

import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def largest_diagonal_prime(nums):
    largest_prime = 0
    n = len(nums)
    for i in range(n):
        if is_prime(nums[i][i]):
            largest_prime = max(largest_prime, nums[i][i])
    if largest_prime > 0:
        return largest_prime
    for i in range(n):
        if is_prime(nums[i][n-i-1]):
            largest_prime = max(largest_prime, nums[i][n-i-1])
    return largest_prime


'''DIAGONAL OF A MATRIX '''
x=[[1,2,3],
[5,6,7],
[8,9,10]]

for i in range(len(x)):
    print(x[i][i])
for i in range(len(x)):
    print((x[i][len(x)-i-1]))