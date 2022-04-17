# solved in 1m
n = int(input())

leonardo = [1, 1]

for i in range(n):
    leonardo.append(leonardo[-1]+leonardo[-2]+1)

print(leonardo[n])
