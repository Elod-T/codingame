# solved in 2m
binary = input().split()

num = [None] * len(binary)
for i, c in enumerate(binary):
    if c in ["1", "yes", "true", "one"]:
        num[i] = "1"
    else:
        num[i] = "0"

print(int("".join(num),2))
