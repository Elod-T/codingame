# solved in 11m

from string import*
a=ascii_letters+"_"
v=input()
if not v[0]in a:print("bad variable name:",v[0]);exit()
a+=digits
for c in v:
    if not c in a:
        print("bad variable name:", c)
        exit()
print("good variable name")

