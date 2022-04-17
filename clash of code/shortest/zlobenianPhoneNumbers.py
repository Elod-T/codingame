# solved in 15m
n="".join(filter(str.isalnum,"".join(input().split())))
if n.startswith("879"):n=n[3:]
print(*map("".join,zip(*[iter(n.zfill(12))]*3)))
