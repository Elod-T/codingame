# solved in 6m
w=list(input())
p=["v"if c in"aeuioAEUIO"else"c"for c in w]
print(str(p==p[::-1]).lower()+" ",*p,sep="")
