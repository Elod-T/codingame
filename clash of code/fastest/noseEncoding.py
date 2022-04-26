# solved in 12m

print(*["".join(a)for a in map(lambda x:["N"if (ord(c)-96)%2==0 else"O"if(ord(c)-96)%3==0 else"S"if(ord(c)-96)%5==0 else"E"for c in list(x)],input().split())])
