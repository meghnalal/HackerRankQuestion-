path = "NESWW"
moves = {
            "N": (0, 1),
            "S": (0, -1),
            "W": (-1, 0),
            "E": (1, 0)
        }
visited = {(0,0)}
x=0
y=0
for c in path:
    dx, dy = moves[c]
    x += dx
    y += dy
    if (x,y ) in visited:
        print(True)

    visited.add((x,y))
