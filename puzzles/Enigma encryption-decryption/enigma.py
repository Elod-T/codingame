# 100%
import sys
from string import ascii_uppercase

abc = ascii_uppercase * 3

operation = input()
num = int(input())
rotors = [input() for i in range(3)]

message = list(input())

if operation == "ENCODE":
    # apply Caesar shift
    message = [abc[abc.index(c) + num + i] for i, c in enumerate(message)]
    print(message, file=sys.stderr)

    # apply rotors
    for rotor in rotors:
        for i, c in enumerate(message):
            message[i] = rotor[abc.index(c)]

        print(message, file=sys.stderr)

    print(*message, sep="")
else:
    # apply rotors backwards
    for rotor in reversed(rotors):
        for i, c in enumerate(message):
            message[i] = abc[rotor.index(c)]

        print(message, file=sys.stderr)

    # apply Caesar shift backwards
    message = [abc[abc.index(c) - num - i + 26] for i, c in enumerate(message)]

    print(*message, sep="")
