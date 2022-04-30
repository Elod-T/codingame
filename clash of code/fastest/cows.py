# solved in 5m

n = int(input())
cows = list(input())
for i in range(n):
    skip = False
    for j, c in enumerate(input()):
        if cows[j] == c:
            print("Invalid")
            skip = True
            break
    if skip:
        continue
    print("Valid")
    
