# solved in 3m
from string import ascii_lowercase


a = list(ascii_lowercase)

i = input().lower()

for c in i:
    if c in a:
        a.remove(c)

if a:
    print(*a)
else:
    print("Pangram")
