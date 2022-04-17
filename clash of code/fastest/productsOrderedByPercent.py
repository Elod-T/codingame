# solved in 3m
d = dict()
n = int(input())
for i in range(n):
    line = input()
    if line in d:
        d[line] += 1
    else:
        d[line] = 1


for key, value in sorted(d.items(),key=lambda x:x[-1],reverse=True):
    print(f"{round(value/n*100,1)}% {key}")
