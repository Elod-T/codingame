# solved in 1m
s = input().split()

if len(s)%2 == 0:
    print(s[len(s)//2-1]+s[len(s)//2])
else:
    print(s[len(s)//2])

