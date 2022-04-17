# solved in 2m
l = input()

num = l.count("+")*4 + l.count("-") + l.count("/") + l.count("*")*5
print(num//4)
