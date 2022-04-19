import sys

n = int(input())

values = []
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    op = "+" if operation == "ADD" else "-" if operation == "SUB" else "*"

    if operation == "VALUE":
        op = ""
        arg_2 = ""

    if "$" in arg_1:
        arg_1 = str(values[int(arg_1[1:])])
    if "$" in arg_2:
        arg_2 = str(values[int(arg_2[1:])])
    
    values.append(eval(arg_1 + op + arg_2))

print(*values, sep="\n")
