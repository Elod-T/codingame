# solved in 2m
n = int(input())
seq = []
for i in input().split():
    sequence = int(i)
    seq.append(sequence)

for i in range(2,n):
    if seq[i] != seq[i-1] + seq[i-2]:
        print("Invalid")
        exit()


print(seq[-1]+seq[-2])
