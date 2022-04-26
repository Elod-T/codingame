# 100%

input()

graph = list(map(int, input().split()))

loss = 0
before = graph[0]
for i, value in enumerate(graph[1:]):
    loss = min(loss, value - before)
    before = max(before, value)

print(loss)

