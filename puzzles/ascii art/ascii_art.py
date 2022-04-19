# 100%
from sys import stderr
from string import ascii_uppercase

l = int(input())
h = int(input())
t = input().upper()

letters = []
for i in range(h):
    row = input()
    letters.append(row)

alphabet = ascii_uppercase + "?"

for i in range(h):
    for char in t:
        if char not in alphabet:
            char = "?"
        index = alphabet.index(char)
        print(letters[i][index * l : (index + 1) * l], end="")
    print()


