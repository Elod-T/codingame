# solved in 2m
crewmate = int(input())
time = int(input())
cooldown = int(input())

x = cooldown * crewmate
print(x <= time)
print(abs(time-x))
