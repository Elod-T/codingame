# solved in 2m
a = int(input())
ar = []
for i in input().split():
    l = int(i)
    ar.append(l)

nl = [0] * a

for i,e in enumerate(ar):
    nl[i] = ar[e]

print(*nl)
