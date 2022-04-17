# solved in 5m
n = int(input())
s = input()

if len(s) % n != 0:
    print("ERROR")
    exit()

for i in range(0, len(s), n):
    print(bin(sum(map(int,s[i:i+n])))[-1],end="")
