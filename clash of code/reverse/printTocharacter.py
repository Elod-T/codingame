# solved in 2m 
from string import ascii_lowercase, ascii_uppercase

l = ascii_lowercase
u = ascii_uppercase
n = "0123456789"

s = input()

for c in s:
    if c in l:
        for i in range(l.index(c)+1):
            print(l[i],end="")
    elif c in u:
        for i in range(u.index(c)+1):
            print(u[i],end="")    
    else:
        for i in range(n.index(c)+1):
            print(n[i],end="")
