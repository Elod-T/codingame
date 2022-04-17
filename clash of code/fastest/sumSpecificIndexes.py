# solved in 50
num_count = int(input())
num = []
for i in input().split():
    number = int(i)
    num.append(number)
index_count = int(input())
s = 0
for i in input().split():
    index = int(i)
    s += num[index]


print(s)
