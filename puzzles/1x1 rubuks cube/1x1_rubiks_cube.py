# 100%

rotations = input().split()
face_1 = input()
face_2 = input()

cube = ["U",
    "L","F","R",
        "D",
        "B"]


rotated = cube


def rotate(direction, cube):
    rotated = [None] * 6
    cubeIndex = []

    if direction == "x":
        # new index  0  1  2  3  4  5
        cubeIndex = [2, 1, 4, 3, 5, 0]
    elif direction == "y":
        # new index  0  1  2  3  4  5
        cubeIndex = [0, 2, 3, 5, 4, 1]
    else:
        # new index  0  1  2  3  4  5
        cubeIndex = [1, 4, 2, 0, 3, 5]

    for a, b in zip(range(6), cubeIndex):
        rotated[a] = cube[b]

    return rotated


for rotation in rotations:
    if rotation.count("'"):
        for i in range(3):
            rotated = rotate(rotation[:-1], rotated)
    else:
        rotated = rotate(rotation, rotated)


print(cube[rotated.index(face_1)])
print(cube[rotated.index(face_2)])

