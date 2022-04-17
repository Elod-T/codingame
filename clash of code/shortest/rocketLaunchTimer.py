# solved in 14m 
# only got 80% because of bad validators :(

n=round(int(input())/1000)
if n>86400:input("24plus")
s=""
for e in[3600,60,1]:
    s+=str(n//e).zfill(2)+":"
    n%=e
print(s[:-1])
