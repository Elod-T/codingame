# 100%
from math import cos, sqrt

lonA = float(input().replace(",","."))
latA = float(input().replace(",","."))
n = int(input())

minDistance = 9999999999
minName = ""
for i in range(n):
    defib = input().replace(",",".").split(";")
    lonB = float(defib[4])
    latB = float(defib[5])

    x = (lonB - lonA) * cos(latA/2 + latB/2)
    y = latB - latA
    d = sqrt(x**2 + y**2) * 6371

    if d < minDistance:
        minDistance = d
        minName = defib[1]

print(minName)
