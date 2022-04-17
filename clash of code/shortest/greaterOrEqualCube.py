# solved in 6m
from math import*
n=int(input())
print(sorted([i for i in range(2*n,n-1,-1)if sqrt(i).is_integer()])[0])
