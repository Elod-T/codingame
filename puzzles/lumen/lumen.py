# 100%

n = int(input())
l = int(input())

room = [input().replace("X", "0").replace("C", str(l)).split() for i in range(n)]


def getNeighbours(x, y):
    neighbours = []
    directions = [-1, 0, 1]

    for a in directions:
        for b in directions:
            nx = x + a
            ny = y + b

            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                neighbours.append([nx, ny])
    return neighbours


light = l
for i in range(l):
    for i, row in enumerate(room):
        for j, pos in enumerate(row):
            if int(pos) == light:
                for x, y in getNeighbours(i, j):
                    room[x][y] = str(max(int(room[x][y]), light - 1))
    light -= 1


print(sum([row.count("0") for row in room]))

