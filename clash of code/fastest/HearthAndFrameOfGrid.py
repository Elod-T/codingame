# solved in 5m
length = int(input())
hearth = -99999999999999
frame = -99999999999999
for i in range(length):
    for j, v in enumerate(input().split()):
        x = int(v)
        if i == j == int(length/2):
            hearth = x

        if i == 0 or i == length-1 or j == 0 or j == length-1:
            frame = max(frame, x)
        
print(str(bool(hearth == frame)).lower())

