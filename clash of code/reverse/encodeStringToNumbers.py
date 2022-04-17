# solved in 6m

# I dont know why, but defining dictionary with values didn't work on codingame :(

w = input()

encode = dict()
encode["s"]="5"
encode["i"]="1"
encode["a"]="4"
encode["o"]="0"
encode["e"]="3"
encode["t"]="7"


decode = dict()
decode["5"]="s"
decode["1"]="i"
decode["4"]="a"
decode["0"]="o"
decode["3"]="e"
decode["7"]="t"


if w.replace(" ","").isalpha():
    for c in w:
        if c in encode:
            print(encode[c],end="")
        else:
            print(c,end="")
else:
    for c in w:
        if c in decode:
            print(decode[c],end="")
        else:
            print(c,end="")
