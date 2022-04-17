# solved in  15m
from itertools import*
n=input()
s=""
d=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
for e in groupby(n):
    p=int(e[0])
    l=len(list(e[-1]))
    if l-1:
        s+=d[l]+" "+d[p]+["s","es"][p==6]
    else:
        s+=d[p]
    s+=" "
print(s[:-1])
