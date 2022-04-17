# solved in 2m
s = input()

decode = {
    "O": "0",
    "L": "1",
    "Z": "2",
    "E": "3",
    "A": "4",
    "S": "5",
    "G": "6",
    "T": "7",
    "B": "8",
    "Q": "9"
}


for c in s:
    if c in decode or c.upper() in decode:
        print(decode[c.upper()],end="")
    else:
        print(c,end="")
