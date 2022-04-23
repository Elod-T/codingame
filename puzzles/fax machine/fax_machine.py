# 100%

w = int(input())
h = int(input())
t = list(map(int, input().split()))

decompressed = "".join([["*", " "][i % 2] * n for i, n in enumerate(t)])

for i in range(0, w*h, w):
    print("|" + decompressed[i : i + w] + "|")

