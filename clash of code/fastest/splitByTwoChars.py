# solved in 3m
ls = input()
ss = input()
p = input().replace(ss,"\n"+ss)

ar = []
for e in p.split(ls):
    for w in e.split(ss):
        ar.append(w)

print(*ar, sep="\n")
