# solved in 5m
d = {}
for i in range(5):
    card = int(input())
    if card in d:
        d[card] += 1
    else:
        d[card] = 1

s = 0
for key, item in d.items():
    if item > 1:
        s += sum(range(1, item))

print(s)
