# solved in 2m
n = int(input())
p, t = [int(i) for i in input().split()]
income = 0
expenses = n * t
passengers = 0
for i in range(n):
    d, u = [int(j) for j in input().split()]
    passengers += u - d
    income += passengers * p

print(income, expenses, int(income >= expenses))
