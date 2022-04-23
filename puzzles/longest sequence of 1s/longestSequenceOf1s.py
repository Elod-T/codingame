# 100%
# "brute force" but it works lol
import sys
from itertools import groupby

b = list(input())

maxOnes = -1
for i in range(len(b)):
    if b[i] == "1": continue

    b[i] = "1"

    for j, e in groupby(b):
        if j == "0": continue
        maxOnes = max(maxOnes, len(list(e)))

    b[i] = "0"

print(maxOnes)
