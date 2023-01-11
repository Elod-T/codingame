# solved in 2m
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def is_prime(number):
    for i in range(2,int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True

n = int(input())
primes = []
for i in range(n):
    x = int(input())
    if is_prime(x):
        primes.append(x)

print(max(primes))
