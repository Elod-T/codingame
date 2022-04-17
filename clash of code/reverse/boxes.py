# solved in 1m
height, width = [int(i) for i in input().split()]
c, cv, ch = input().split()


print(c + ch*(width-2) + c)

for i in range(height-2):
    print(cv + " "*(width-2) + cv)

print(c + ch*(width-2) + c)
