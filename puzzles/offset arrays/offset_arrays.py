# 100%

n = int(input())

arrays = dict()
for i in range(n):
    assignment = input()

    name, rest = assignment.split("[")
    start = int(rest.split("..")[0])
    end = int(rest.split("..")[1].split("]")[0])

    array = list(map(int, assignment.split("=")[1].split()))
    arrays[name] = dict(zip(range(start, end + 1), array))


*expr, value = input().replace("]", "").split("[")

value = int(value)
for exp in expr[::-1]:
    value = arrays[exp][value]

print(value)

