# solved in 7m
I=input
print(sum(map(lambda x:int(x)if int(x)%2==0 else-int(x),(I()+" "+I()+" "+I()).split())))

