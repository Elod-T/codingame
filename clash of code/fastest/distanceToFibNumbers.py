# solved in 1m
n = int(input())

d = 9999
fib = [1, 1]
for i in range(n):
    fib.append(fib[-1]+fib[-2])

for c in fib:
    d = min(d, abs(n-c))

print(d)
