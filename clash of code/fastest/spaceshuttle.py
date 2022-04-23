# solved in 3m
n = int(input())
for i in range(n):
    x, y, z = [float(j) for j in input().split()]
    print("OPEN" if math.sqrt(x**2+y**2+z**2) >= 9 else "WAIT") 
