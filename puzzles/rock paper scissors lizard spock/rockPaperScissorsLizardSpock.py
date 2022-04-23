# 100%

n = int(input())

players = []

for i in range(n):
    inputs = input().split()
    num = int(inputs[0])
    sign = inputs[1]

    players.append([num, sign])

loseCondition = {
    "CP": "P",
    "PR": "R",
    "RL": "L",
    "LS": "S",
    "SC": "C",
    "CL": "L",
    "LP": "P",
    "PS": "S",
    "SR": "R",
    "RC": "C"
}

matches = [[] for i in range(n+1)]

while len(players) > 1:
    toRemove = []
    for i in range(0, len(players), 2):
        p1num, p1sign = players[i]
        p2num, p2sign = players[i+1]

        matches[p1num].append(p2num)
        matches[p2num].append(p1num)

        if p1sign == p2sign:
            toRemove.append([[p1num, p2num][p2num > p1num], p1sign])

        else:
            matchup = p1sign + p2sign
            if matchup in loseCondition:
                loserSign = loseCondition[matchup]
            else:
                loserSign = loseCondition[matchup[::-1]]

            if p1sign == loserSign:
                toRemove.append(players[i])
            else:
                toRemove.append(players[i + 1])

    for item in toRemove:
        players.remove(item)

print(players[0][0])
print(*matches[players[0][0]])

