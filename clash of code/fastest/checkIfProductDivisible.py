# solved in 3m
n = int(input())
d = int(input())
sol = 1
for i in range(n):
    x = int(input())
    sol *= x % d

print("Perfect" if sol % d==0 else "Imperfect")

