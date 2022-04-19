# 50%
import sys
import math

tx, ty = map(int, input().split())

# game loop
while True:
    strikes, enemyCount = map(int, input().split())

    enemies = []

    for i in range(enemyCount):
        x, y = map(int, input().split())
        enemies.append([x, y])


    print("Enemies' positions:", enemies, file=sys.stderr)

    distance = 9999
    closestPos = [-1, -1]
    # closest enemy
    for enemy in enemies:
        d = math.sqrt(abs(tx - enemy[0])**2 + abs(ty - enemy[1])**2)
        if d < distance:
            distance = d
            closestPos = enemy
    print("Closest enemy distance:", distance, "position:", closestPos , file=sys.stderr)
    
    if distance <= 2:
        print("STRIKE")
    else:
        # average enemy position
        avx = sum(e[0] for e in enemies) // len(enemies)
        avy = sum(e[1] for e in enemies) // len(enemies)
        print("Average enemy position:", avx, avy, file=sys.stderr)

         
        # same as in episode 1
        command = ""

        if avy < ty:
            command += "N"
            ty -= 1
        elif avy > ty:
            command += "S"
            ty += 1
            
        if avx < tx:
            command += "W"
            tx -= 1
        elif avx > tx:
            command += "E"
            tx += 1

        if command == "":
            command = "WAIT"

        print(command)
    
