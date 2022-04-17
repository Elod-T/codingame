# solved in 3m
arr = []
sol = 0
for i in range(9):
    line = "."+input()
    last = line[0]

    for i, c in enumerate(line):
        if i == 0 or i == len(line)-1: continue

        if line[i-1] == "." and c == "#" and line[i+1] == "#":
            sol += 1
        
    arr.append(line)

arr.insert(0, "."*len(arr[0]))
for i in range(len(arr[0])):
    for j, line in enumerate(arr):
        if arr[j-1][i] == "." and line[i] == "#" and arr[j+1][i] == "#":
            sol += 1

print(sol) 
