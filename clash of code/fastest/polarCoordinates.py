# solved in 12m
import numpy

x = True
width, height = [int(i) for i in input().split()]
for i in range(height):
    row = input()
    for j,c in enumerate(row):
        if c == "*":
            print(round(numpy.sqrt(j**2 + i**2),1), round(numpy.degrees(numpy.arctan2(i,j)),1) )
            x = False
if x: print("Dead")
