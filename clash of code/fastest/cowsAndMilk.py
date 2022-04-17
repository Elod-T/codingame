# solved in 2m
s = input().split()

cows = s.count("COWS")
milk = s.count("MILK")

print("no "+str(cows) if cows == milk else str(cows) + " " + str(milk))
