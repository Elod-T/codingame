# solved in 2m
sentence = input().split()

s = ""
for word in sentence:
    counter = 0
    for c in word:
        if c.lower() in "aeoui":
            counter += 1
    s += str(counter) + " "

print(s[:-1])
