# solved in 3m
w = input()
c = input()

s = ""
for i in range(len(w)):
    if i % 2:
        s += w[::-1] + " \n"[c=="D"]
    else:
        s += w + " \n"[c=="D"]

print(s[:-1])
