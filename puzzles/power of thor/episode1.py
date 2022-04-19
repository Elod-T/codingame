# 100%
x, y, tx, ty = map(int, input().split())

# game loop
while True:
    remaining_turns = int(input())

    command = ""

    if y < ty:
        command += "N"
        ty -= 1
    elif y > ty:
        command += "S"
        ty += 1
    
    if x < tx:
        command += "W"
        tx -= 1
    elif x > tx:
        command += "E"
        tx += 1

    print(command)
