# solved in 5m
n = int(input())
for i in range(n):
    wizard = list("wizard")
    names = input().lower()
    for c in names:
        try:
            wizard.remove(c)
        except:
            pass

    print("Not" if len(wizard) else "Is", "a wizard")
