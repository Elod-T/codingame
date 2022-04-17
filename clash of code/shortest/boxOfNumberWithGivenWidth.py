# solved in 13m
x=int(input())
y=int(input())
for i in range(0,x,y):print(*range(1,x+1)[i:i+y])
