# solved in 50s
n = int(input())
odd = []
for i in range(n):
    line = input()
    if i%2 == 0:
        print(line)
    else:
        odd.append(line)

print(*odd,sep="\n")
