# solve in 2m
len_t = int(input())
j=0
for i in input().split():
    x = int(i)
    if j < len_t-1:
        print(x,x*".",sep="",end="")
    else:
        print(x,sep="",end="")
    j += 1


