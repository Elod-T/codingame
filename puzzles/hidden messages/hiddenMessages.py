# 100%
import numpy

pixels = "".join(list(numpy.array([[bin(int(j))[2:][-1] for j in input().split()] for i in range(int(input().split()[1]))]).flatten()))

for i in range(0, len(pixels), 8):
    print(end=chr(int(pixels[i : i + 8], 2)))
