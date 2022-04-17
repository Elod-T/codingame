# solved in 44s
n_1, n_2 = input().split()

for a,b in zip(n_1,n_2):
    print(int(int(a) or int(b)),end="")
