# solved in 6m
n = input()

accepted = True

if n[0].isnumeric() or n[-1].isnumeric():
    accepted = False

wasNum = False
lastNum = False
for c in n:
    if c.isnumeric() and not wasNum:
        wasNum = True
    elif c.isalpha() and wasNum and not lastNum:
        lastNum = True
    elif c.isnumeric() and lastNum:
        accepted = False
        break


count = 0

for c in n:
    if accepted and c.isnumeric():
        count += 1
    elif not accepted and c.isalpha():
        count += 1

print(count)
