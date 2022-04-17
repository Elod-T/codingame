# solved in 5m
import math
n=int(input())
print([i for i in range(n)if math.gcd(i,n)==1][-2])
