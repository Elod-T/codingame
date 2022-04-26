# solved in 3m 

number = int(input())

for i in range(number):
    if i%2:
        print(*map(str, range(number-i, 0, -1)), sep="")
    else:
        print(*map(str, range(1, number-i+1)), sep="")
