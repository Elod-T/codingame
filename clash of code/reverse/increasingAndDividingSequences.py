# solved in 3m
l = int(input())
m = int(input())
n = int(input())

print(*[l+i*m for i in range(n)])
print(*[int(l/m**i) for i in range(n)])  
