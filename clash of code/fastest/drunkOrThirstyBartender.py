# solved in 2m
n = int(input())
percentage = int(input())
totaltip = 0
totalbill = 0
for i in range(n):
    bill, tip = [float(j) for j in input().split()]
    totaltip += tip
    totalbill += bill

print(["DRUNK","THIRSTY"][totalbill/100*percentage>totaltip])

