# 100%

from itertools import cycle


n = int(input())

invalid = []
for i in range(n):
    unchanged = input()
    isbn = list(unchanged)
    lenght = len(isbn)

    if (lenght != 10 and lenght != 13) or (lenght != 10 and isbn.count("X")):
        invalid.append(unchanged)
        continue

    try:
        isbn = list(map(lambda x: int(x.replace("X", "10")), isbn))
    except:
        invalid.append(unchanged)
        continue

    if len(isbn) == 10:
        if isbn[-1] != (11 - sum([a*b for a, b in (zip(range(10, 1, -1), isbn[:-1]))]) % 11) % 11:
            invalid.append(unchanged)
            continue
    else:
        if isbn[-1] != (10 - sum([a*b for a, b in (zip(cycle([1, 3]), isbn[:-1]))]) % 10) % 10:
            invalid.append(unchanged)
            continue

print(f"{len(invalid)} invalid:", *invalid, sep="\n")

