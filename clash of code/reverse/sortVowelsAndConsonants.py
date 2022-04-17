# solved in 1m
message = input()

v = "aeuioyAEUIOY"

for c in message:
    if c in v:
        print(end=c)
print()
for c in message:
    if c not in v and c.isalpha():
        print(end=c)

