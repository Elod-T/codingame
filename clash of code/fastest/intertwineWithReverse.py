# solved in 5m
s = list(input())

for a,b in zip(s,s[::-1]):
    print(a + b,end="")

