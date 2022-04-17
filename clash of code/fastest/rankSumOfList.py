# solved in 14m
responses = int(input())
d= dict()
for i in range(responses):
    line = input().split()
    for i, c in enumerate(line):
        try:
            d[c] += i+1
        except Exception:
            d[c] = i+1

for key, value in sorted(d.items(),key=lambda k:(k[1], k[0])):
    print(key, value)
