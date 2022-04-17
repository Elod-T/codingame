# solved in 13m
x = int(input())
if x==0:input("NONE")
c=[]
for i in range(x):
    n,s,e=input().split()
    c.append((float(e)/float(s),n))
print(max(c)[-1])
