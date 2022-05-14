n = int(input())
for i in range(n):
    su = ""
    p0, p1 = [bin(int(j))[2:] for j in input().split()]
    if len(p0) > len(p1):
        p1 = p1.zfill(len(p0))
    else:
        p0 = p0.zfill(len(p1))
    for a,b in zip(p0, p1):
        su += str(int(a) + int(b))
    print(su)
