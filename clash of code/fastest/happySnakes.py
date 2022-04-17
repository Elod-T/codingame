# solved in 3m
n = int(input())
happy = 0
for i in range(n):
    snake = input()
    if snake.startswith(">-") or snake.endswith("-<"):
        happy += 1

# x/100 = happy/n
if happy:
    print(int(happy/n*100), "%", sep="")
else:
    print("0%")
    
