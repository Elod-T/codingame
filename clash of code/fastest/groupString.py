# solved in 2m
import itertools
s = input()

sol=""
for _,l in itertools.groupby(s):
    sol+="".join(list(l))+" "
print(sol[:-1])
