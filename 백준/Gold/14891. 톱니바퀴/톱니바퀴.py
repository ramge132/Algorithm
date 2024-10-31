from collections import deque

def rotate(gear, direction):
    if direction == 1:
        gear.rotate(1)
    elif direction == -1:
        gear.rotate(-1)

gears = [deque(map(int, input())) for _ in range(4)]
K = int(input())
rotations = [tuple(map(int, input().split())) for _ in range(K)]

for num, direction in rotations:
    num -= 1
    directions = [0] * 4
    directions[num] = direction

    for i in range(num, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            directions[i - 1] = -directions[i]
        else:
            break

    for i in range(num, 3):
        if gears[i][2] != gears[i+1][6]:
            directions[i+1] = -directions[i]
        else:
            break

    for i in range(4):
        if directions[i] != 0:
            rotate(gears[i], directions[i])

score = 0
for i in range(4):
    if gears[i][0] == 1:
        score += 2 ** i

print(score)