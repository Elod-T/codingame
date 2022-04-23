# 100%
import numpy

board = [list(map(int, input().split())) for i in range(9)]

validate = lambda array: all([array.count(i) for i in range(1, 10)])


for row in board:
    if not validate(row):
        input("false")


for i in range(9):
    array = [row[i] for row in board]
    if not validate(array):
        input("false")


for i in range(0, 7, 3):
    for j in range(0, 7, 3):
        array = list(numpy.array([board[j + k][i:i+3] for k in range(3)]).flatten()) # 2d array so we use numpy to flatten it and then we convert it back
        if not validate(array):
            input("false")

print("true")
