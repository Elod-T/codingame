# solved in 10m
s=input()
p=1
l=len(s)
for i in range(l):
    if p<l:print(end=s[i+p-1]);p+=i+1
