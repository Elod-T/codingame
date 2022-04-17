# solved in 27s
n_1 = input()
n_2 = input()

for a,b in zip(n_1,n_2):
    print(int(int(a) and int(b)),end="")
