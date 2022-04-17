# solved in 29s
n = int(input())

for i in range(n):
    if math.factorial(i) == n:
        print(i)
        exit()

