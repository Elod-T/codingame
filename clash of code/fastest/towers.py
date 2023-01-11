# solved in 5m
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
numbers = list(map(int, input().split()))

maxHeight = max(numbers)

for height in range(maxHeight, 0, -1):
    line = ""
    for number in numbers:
        if number == height:
            line += "*** "
        elif number >= height:
            line += "* * "
        else:
            line += "    "
    print(line[:-1])

