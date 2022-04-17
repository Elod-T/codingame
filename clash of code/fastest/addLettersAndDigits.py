# solved in 5m
s = input()

w = ""
d = ""
for c in s:
    if c.isalpha():
        w += str(bin(ord(c))[2:])
    else:
        d += str(bin(int(c))[2:])      

print(w+d)
