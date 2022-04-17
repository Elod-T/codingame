# solved in 2m

n = int(input())

s = ""
while n-1:
    s += str(n) + " "

    if n%2:
        n *= 3
        n += 1
    else:
        n //=2


print(s + "1")

