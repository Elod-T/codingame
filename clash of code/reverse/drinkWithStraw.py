# solved in 3m
drink = input()
straw = bool(int(input()))

pattern = [
    r"____?____",
    r"\       /",
    r" \  ?  /",
    r"  \___/"
]

pattern[0] = pattern[0].replace("?", "|" if straw else "_")
pattern[2] = pattern[2].replace("?", drink)

print(*pattern, sep="\n")

