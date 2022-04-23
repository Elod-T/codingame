# 66%

a1 = int(input())
n = int(input())

sequence = [a1] + [0 for i in range(n)]

for i in range(n):
    for j in range(i - 1, -1, -1):
        if sequence[j] == sequence[i]:
            sequence[i + 1] = i - j
            break

print(sequence[n - 1])
