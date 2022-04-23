# solved in 1m
n = int(input())  # The numbers of paths the train can take
values = []
for i in range(n):
    # q: The number of persons on the path
    # v: The individual value of each person on the path
    q, v = [int(j) for j in input().split()]

    values.append(q * v)



print(values.index(min(values))+1)
