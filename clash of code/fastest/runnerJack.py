# solved in 3m
k = int(input())

walked = 0

i = 1
while walked < k:
    walked += 1/i
    i += 1

print(i-1)
