# 83%
# passed all test cases, but not all validators :(

import sys

w, h = map(int, input().split())
ticket =[list(input()) for i in range(h)]


for i in range(0, w, 3):
    row = 1
    column = i
    print(ticket[0][i], file=sys.stderr)
    while not ticket[row][column].isalnum():
        # ---- DEBUG ----
        toPrint = ticket
        toPrint[row][column] = "X"
        print(*["".join(r) for r in toPrint], sep="\n", file=sys.stderr)
        print(file=sys.stderr)
        # ---- DEBUG ----

        if column > 0 and ticket[row][column - 1] == "-":
            column -= 3

        elif column < w - 1 and ticket[row][column + 1] == "-":
            column += 3

        row += 1
        
        
    print(ticket[0][i], ticket[row][column], sep="")
