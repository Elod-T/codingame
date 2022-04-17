# solved in 25s
n = int(input())
for i in range(n):
    x = [int(j) for j in input().split()]
    x.remove(min(x))
    x.remove(max(x))
    print(x[0])
    
