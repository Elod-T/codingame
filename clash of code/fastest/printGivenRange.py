# solved in 2m
n = int(input())
s, e = map(int,input().split("-"))

print(*list(range(s+n, e+1, n)))
