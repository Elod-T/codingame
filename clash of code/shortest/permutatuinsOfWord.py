# solved in 12m
import itertools
input()
x=list(input())
print(*sorted(["".join(c)for c in set(itertools.permutations(x,len(x)))]))
