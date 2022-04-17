# solved in 2m
import sys
import math
from string import ascii_lowercase, ascii_uppercase

l = ascii_lowercase
u = ascii_uppercase

case_or_trick = input().lower()
n = int(input())
if n > 26 or n < 1:
    print("ERROR")
else:
    if case_or_trick == "upper":
        print(" ".join(u[:n]))
    else:
        print(" ".join(l[:n]))
