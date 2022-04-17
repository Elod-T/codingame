h = int(input())
r = int(input())
s_1 = int(input())
s_2 = int(input())

size = min(abs(s_1 - s_2), abs(360 - abs(s_1 - s_2)))

print(round(h*r*r*3.14 / 360 * size, 1))

