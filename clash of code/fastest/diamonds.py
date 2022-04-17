# solved in 3m
n = int(input())

print("#"*n)


for i in range(n):
    print((n-i-1)*" "+"#"*(i*2+1))

for i in range(n):
    print(i*" "+"#"*((n-i)*2-1))

