n = int(input())
lastNum, lastCol = -1, ""
mistakes = -1
for i in range(n):
    inputs = input().split()

    v = int(inputs[0])
    c = inputs[1]

    if lastNum != v and lastCol != c:
        mistakes += 1

    lastNum = v
    lastCol = c

print("Correct" if mistakes <= 0 else f"Incorrect:{mistakes}")

