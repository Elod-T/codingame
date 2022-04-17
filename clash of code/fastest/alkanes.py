# solved in 3m
n = int(input())
c = 0
h = 0
for i in range(n):
    line = input()
    c += line.count("C")
    h += line.count("H")


if c == 1 and h == 4:
    print("methane")
elif c == 2 and h == 6:
    print("ethane")
elif c == 3 and h == 8:
    print("propane")
elif c == 4 and h == 10:
    print("butane")
elif c == 5 and h == 12:
    print("pentane")
else:
    print("NONE")
