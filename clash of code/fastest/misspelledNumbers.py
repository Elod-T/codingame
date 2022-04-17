# solved in 2m
n = int(input())
for i in range(n):
    number = input()
    try:
        print(int(number))
    except:
        print(int(["","-"][number.count("-")%2]+number.replace("-","").replace("+","")))
