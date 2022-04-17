# solved in 2m
string = input().lower().replace(" ","")

d = {}

for c in string:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

s = ""
for key, value in d.items():
    s += f"{key}:{value} "


print(s.strip())
