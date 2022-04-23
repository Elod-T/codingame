# solved in 1m
character = input()
x = int(input())


for i in range(x):
    print(" "*(x - i - 1) + character*(i*2 + 1))
