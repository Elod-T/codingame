# solved in 1m
num = int(input())

print(str(num == sum([int(i)**len(str(num)) for i in str(num)])).lower())

