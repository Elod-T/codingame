# 100%
transitions = dict()
def checkWord(word, start, ends):
    state = start

    for c in word:
        if state+c in transitions:
            state = transitions[state+c]
        else:
            return False

    return state in ends


_input = input()
states = input()
number_of_transitions = int(input())


for i in range(number_of_transitions):
    From, char, to = input().split()
    transitions[From+char] = to


start_state = input()
end_states = input().split()
number_of_words = int(input())

for i in range(number_of_words):
    print(str(checkWord(input(), start_state, end_states)).lower())

