# 100%

board = [list(input()) for i in range(3)]


def printBoard():
    print(*["".join(row) for row in board], sep="\n")
    exit()


for i, row in enumerate(board):
    if row.count("O") == 2 and row.count(".") == 1:
        board[i] = list("O"*3)
        printBoard()

    
for i in range(3):
    column = [row[i] for row in board]
    if column.count("O") == 2 and column.count(".") == 1:
        for j, row in enumerate(board):
            board[j][i] = "O"
        printBoard()
    


diagonal = [board[i][i] for i in range(3)]
if diagonal.count("O") == 2 and diagonal.count(".") == 1:
    for i in range(3):
        board[i][i] = "O"
    printBoard()


diagonal = [board[i][3-i-1] for i in range(3)]
if diagonal.count("O") == 2 and diagonal.count(".") == 1:
    for i in range(3):
        board[i][3-i-1] = "O"
    printBoard()


print("false")

