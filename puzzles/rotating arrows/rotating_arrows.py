# 100%

w, h = map(int, input().split())
x, y = map(int, input().split())

grid = [list(input()) for i in range(h)]

move = "^>v<^"

rotations = 0
start = (x, y)
while True:
    rotations += 1
    arrow = grid[y][x]

    nextArrow = move[move.index(arrow)+1]

    grid[y][x] = nextArrow

    if nextArrow == ">":
        x += 1
    elif nextArrow == "<":
        x -= 1
    elif nextArrow == "^":
        y -= 1
    else:
        y += 1

    if x < 0 or y < 0 or x > w-1 or y > h-1 or (x, y) == start:
        print(rotations)
        exit()


