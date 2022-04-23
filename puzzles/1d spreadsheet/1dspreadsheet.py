# 100%
import sys

n = int(input())

values = [input().split() for i in range(n)]
print(values, file=sys.stderr)
while sum(map(len, values)) != n:
    for i, value in enumerate(values):
        if len(value) == 1 or (value[1].count("$") and len(values[int(value[1][1:])]) > 1) or (value[2].count("$") and len(values[int(value[2][1:])]) > 1):
            continue

        operation, arg1, arg2 = value

        op = "+" if operation == "ADD" else "-" if operation == "SUB" else "*" if operation == "MULT" else ""

        if operation == "VALUE":
            arg2 = ""

        if arg1.count("$"):
            arg1 = eval("str(values[" + arg1[1:] + "][0])")

        if arg2.count("$"):
            arg2 = eval("str(values[" + arg2[1:] + "][0])")

        print(arg1, op, arg2, file=sys.stderr)
        values[i] = [eval(arg1 + op + arg2)]

        print(values, file=sys.stderr)

print(*[value[0] for value in values], sep="\n")
