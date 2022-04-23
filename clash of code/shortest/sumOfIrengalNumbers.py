# solved in 13m
n,*m=open(0)
print(sum([int(n)for n in m[0].split()if len([c for i,c in enumerate(n)if n.count(str(i))==int(c)])==len(n)]))

