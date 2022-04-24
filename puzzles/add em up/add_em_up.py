# 100%

n = int(input())
cards = sorted(list(map(int, input().split())))

cost = 0
while len(cards) > 1:
    newCard = cards[0] + cards[1]
    cost += newCard

    cards.pop(0)
    cards.pop(0)

    cards.append(newCard)
    cards.sort()

print(cost)

