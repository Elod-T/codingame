# solved in 3m
n = int(input())
ar = []
for i in input().split():
    u = int(i)
    ar.append(u)

c = ar[1]-ar[0]
l = ar[0]    
for i in range(n):
    if i == 0: continue

    if ar[i] - ar[i-1] != c:
        print("NOT CONSTANT")
        exit()

print(c)
