# solved in 3m
degrees = int(input())

for i in range(3,degrees*3):
    if int((i-2)*180/i) == degrees:
        input(i)
