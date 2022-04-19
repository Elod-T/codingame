# 100%
import sys

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

graph = [[] for i in range(n)]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    graph[n1].append(n2)
    graph[n2].append(n1)

exits = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    exits.append(ei)


def distance(a, b):
    queue = [(a, 0)]
    visited = [False] * n
    visited[a] = True
    path = [None] * n
    _distance = [None] * n
    while queue:
        node, dist = queue.pop(0)
        for i in graph[node]:
            if not visited[i]:
                queue.append((i, dist + 1))
                visited[i] = True
                path[i] = node
                _distance[i] = dist + 1
    return (path[b], _distance[b])



# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    print(graph, file=sys.stderr)

    distances = []
    for _exit in exits:
        distances.append((distance(_exit, si)[1], _exit))

    print(distances, file=sys.stderr)

    closestExit = sorted(distances)[0][1]
    print(closestExit, file=sys.stderr)


    print(distance(closestExit, si)[0], si)

    
