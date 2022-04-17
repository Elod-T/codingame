# solved in 1m
n = int(input())
ar = []
for i in input().split():
    x = int(i)
    ar.append(x)
m = int(input())
for i in range(m):
    start, end = [int(j) for j in input().split()]
    print(sum(ar[start:end+1]))
