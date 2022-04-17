# solved in 40s
t = input()

for i in range(0, len(t), 2):
    print(t[i:i+2][::-1],end="")
