# solved in 6m
s = input()

try:
    if int(s) >= 0:
        print(sum([int(e) for i,e in enumerate(s) if i != 0]) * int(s[0]))
    else:
        print(sum([int(e) for i,e in enumerate(s) if i > 1]) * int(s[:2]))

except:
    print("INVALID")
