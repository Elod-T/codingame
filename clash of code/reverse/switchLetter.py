# solved in 1m
s = input()

e = list(set(s))

print(s.replace(e[0], " ").replace(e[-1],e[0]).replace(" ",e[-1]))
