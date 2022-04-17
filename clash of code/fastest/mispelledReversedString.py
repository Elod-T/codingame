# solved in 50s

line_1 = input()
line_2 = input()[::-1]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

c = 0

for a,b in zip(line_1,line_2):
    c += 1 if a != b else 0

print(c)

