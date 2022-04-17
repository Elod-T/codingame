# solved in 1m
from itertools import groupby

s = list(input())

for i,e in groupby(s):
    print(len(list(e)),i,sep="",end="")
