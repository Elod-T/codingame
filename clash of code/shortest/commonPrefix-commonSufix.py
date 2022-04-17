# solved in 12m
a=input()
b=input()
print(sum([1 for i in range(len(a))if a.startswith(b[:i])])-sum([1 for i in range(len(a))if a[::-1].startswith(b[::-1][:i])]))

