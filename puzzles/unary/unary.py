# 100%

from itertools import groupby

message = input()

message = "".join([bin(ord(c))[2:].zfill(7) for c in message])

encoded = ""

for i,e in groupby(message):
    block = "0 " if i == "1" else "00 "
    block += "0" * len(list(e)) + " "
    encoded += block


print(encoded[:-1])
