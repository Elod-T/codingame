# solved in 2m
input_count = int(input())
for i in range(input_count):
    ipaddress, end = input().split("/")
    print(2 ** abs(int(end) - 32) - 2)
