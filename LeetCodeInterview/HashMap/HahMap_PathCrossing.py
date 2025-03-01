'''
Path Crossing
'''

'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', 
each representing moving one unit north, south, east, or west, respectively. 
You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a 
location you have previously visited. Return false otherwise.
'''

from collections import defaultdict

path = "NESWW"

moves = {
    "N": (0, 1),
    "S": (0, -1),
    "W": (-1, 0),
    "E": (1, 0)
}

visited= {(0,0)}
x=0
y=0

for i in path:
    dx, dy = moves[i]
    x += dx
    y += dy
    if (x, y) in visited:
        print (True)
    visited.add((x, y))

