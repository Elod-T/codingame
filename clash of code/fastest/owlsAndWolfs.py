# solved in 1m
w, h = [int(i) for i in input().split()]
wolfs = 0
owls = 0
for i in range(h):
    row = input()
    wolfs += row.count(r"|\_/|")
    owls += row.count(r"(oo)")

print(wolfs)
print(owls)
