"""

2379. Minimum Recolors to Get K Consecutive Black Blocks

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of
the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

Example:
    Input: blocks = "WBBWWBBWBW", k = 7
    Output: 3
    Explanation:
    One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
    so that blocks = "BBBBBBBWBW".
    It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
    Therefore, we return 3.

"""

''' I think thi solution without pointer is the best one 
    as it removes the need to count all the time'''

blocks = "WBBWWBBWBW"
k = 7

count = blocks[:k].count('W')
min_count = count

for i in range(len(blocks)-k):
    if blocks[i] == 'W':
        count -= 1
    if blocks[i+k] == 'W':
        count += 1
    if count < min_count:
        min_count = count
print(min_count)

'''Solving with pointer method'''

blocks = "WBBWBWWBWBW"
k = 3
i = 0
j = 0
min_count = 0 
count = 0
minOps = 1e9


while j < (len(blocks)):

    if j-i+1 < k:
        if blocks[j] == 'W':
            count += 1
        j += 1
        min_count = count

    if j-i+1 == k:

        if blocks[i] == 'W':
            count -= 1
        if blocks[j+1] == 'W' and j + 1 < len(blocks):
            count += 1
        if count < min_count:
            min_count = count
        i += 1
        j += 1
print(min_count)


