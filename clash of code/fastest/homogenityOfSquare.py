# solved in 8m
n = int(input())

h = 0

prev = ""

for i in range(n):
    line = input()
    for j in range(n-1):
        if line[j] == line[j+1]:
            h += 1
        else:
            h -= 1

    if i == 0:
        prev = line
    else:
        for j in range(n):
            if line[j] == prev[j]:
                h += 1
            else:
                h -= 1
        prev = line


print(h)
