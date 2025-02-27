'''

2352. Equal Row and Column Pairs
'''
'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) 
such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in 
the same order (i.e., an equal array).
'''
from collections import defaultdict
grid = [[13,13],[13,13]]

transposed_matrix = [[row[i] for row in grid] for i in range(len(grid[0]))]


grid_row= defaultdict(int)
grid_col= defaultdict(int)

for i in transposed_matrix:
    key = tuple(i)
    grid_col[key] += 1


# Fill grid_horizontal correctly
for x in grid:
    key = tuple(x)
    grid_row[key] += 1

ans= 0

# Check if any list in grid_horizontal is present in grid_vertical
for z in grid_row.keys():
    if z in grid_col:
        ans += grid_row[z] * grid_col[z]

print(ans)
