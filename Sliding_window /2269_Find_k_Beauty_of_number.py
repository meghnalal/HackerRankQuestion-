"""
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string
that meet the following conditions:

It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:

Leading zeros are allowed.
0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.

Example:
    Input: num = 240, k = 2
    Output: 2
    Explanation: The following are the substrings of num of length k:
    - "24" from "240": 24 is a divisor of 240.
    - "40" from "240": 40 is a divisor of 240.
    Therefore, the k-beauty is 2.
"""
''' my method by initialising the first window and checking the others '''
num = 240
k = 2
count = 0

num_str = str(num)
window = num_str[:k]
if num % int(window) == 0:
    count += 1

for i in range(len(num_str)-k):
    next_window = num_str[i+1:i+k+1]
    if int(next_window) != 0 and num % int(next_window) == 0 :
        count += 1

print (count)

''' with pointer method not neccesarily needed '''

num = 240
k = 2
num_str = str(num)
j = 0
i = 0
count = 0
while j < len(num_str):
    if j-i+1 < k:
        j += 1
    if j-i+1 == k:
        current_window = int(num_str[i:j+1])
        if current_window != 0 and num % current_window == 0 :
            count += 1
        j += 1
    if j-i+1 > k:
        i += 1

print(count)



''' cleaner loop solution  '''


def k_beauty(num, k):
    num_str = str(num)
    count = 0

    for i in range(len(num_str) - k + 1):
        substring = num_str[i:i + k]
        substring_num = int(substring)

        if substring_num != 0 and num % substring_num == 0:
            count += 1

    return count

# Test the function with the given example
num = 240
k = 2
print(k_beauty(num, k))  # Output: 2


