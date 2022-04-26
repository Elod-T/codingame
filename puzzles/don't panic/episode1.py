# 100%

import sys
import math

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = map(int, input().split())

goals = sorted([list(map(int, input().split())) for _ in range(nb_elevators)] + [[exit_floor, exit_pos]])

# game loop
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT

    goal = goals[clone_floor][1]


    if (goal < clone_pos and direction == "RIGHT") or (goal > clone_pos and direction == "LEFT"):
        print("BLOCK")
    else:
        print("WAIT")

