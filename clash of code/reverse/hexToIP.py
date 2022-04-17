# solved in 2m
h = input()[2:]

ip = []
for i in range(0, len(h), 2):
    ip.append(int(h[i:i+2],16))

print(*ip, sep=".")

