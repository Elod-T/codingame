# solved in 5m
n = int(input())
l = input()

p = -1

counter = 0
for i,c in enumerate(l):
    if c == "1":
        if counter == 0:
            p = i
            counter += 1
        elif counter == 1:
            p = i-p
            counter += 1

last = -1
for i,c in enumerate(l):
    if last == -1 and c == "1":
        last = i
        continue
    
    if c == "1":
        if i - last != p:
            print("false")
            exit()
        last = i

print(p)

