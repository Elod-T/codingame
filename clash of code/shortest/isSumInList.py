# solved in 10m
I=input
n=int(I())
I()
a=set(map(int,input().split()))
for c in a:
    if n-c in a:
        print(*sorted([c,n-c]));exit()
print("N/A")
