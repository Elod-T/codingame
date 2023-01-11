# solved in 2m
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, h, pf, ph = map(int, input().split())
price = l * h * pf + h * ph
print(int(price * 1.1))
