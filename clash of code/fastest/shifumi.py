# solved in 1m
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

o = input()

play = {
    "Scissors": "Stone",
    "Stone": "Hand",
    "Hand": "Scissors"
}

try:
    print(play[o])
except KeyError:
    print("Error")
