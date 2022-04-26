# 100%

board = []

king = (0, 0)
enemy = ("P", 0, 0)

for i in range(8):
    line = input().split()

    if line.count("_") < 8:
        for j, c in enumerate(line):
            if c == "K":
                king = (i, j)
            elif c != "_":
                enemy = (c, i, j)

    board.append(line)


enemyType, ex, ey = enemy
x, y = king

checkConditions = {
    "R": x == ex or y == ey,
    "B": abs(ex - x) == abs(ey - y),
    "N": (abs(ex - x) == 2 and abs(ey - y) == 1) or (abs(ex - x) == 1 and abs(ey - y) == 2)
}
checkConditions["Q"] = checkConditions["R"] or checkConditions["B"] # can't be added directly in definition

print("No " * (1-checkConditions[enemyType]) + "Check")

