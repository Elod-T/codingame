# 100%

for i in range(int(input())):
    card = input().replace(" ", "")
    print("NO" if (sum(map(lambda x: int(x)*2 if int(x)*2 < 10 else int(x)*2-9, card[::2])) + sum(map(int, card[::-1][::2]))) % 10 else "YES")
