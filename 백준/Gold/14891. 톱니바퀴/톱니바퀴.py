from collections import deque

def rotation(gear, direction):
    if direction == 1:
        gear.rotate(1)
    elif direction == -1:
        gear.rotate(-1)

gear = [deque(map(int, input())) for _ in range(4)]
K = int(input())
rotations = [tuple(map(int, input().split())) for _ in range(K)]

for num, direction in rotations:
    num -= 1
    directions = [0] * 4
    directions[num] = direction

    # 왼쪽
    for i in range(num, 0, -1):
        if gear[i][6] != gear[i-1][2]:
            directions[i-1] = -directions[i]

    # 오른쪽
    for i in range(num, 3):
        if gear[i][2] != gear[i+1][6]:
            directions[i+1] = -directions[i]

    for i in range(4):
        if directions[i] != 0:
            rotation(gear[i], directions[i])

result = 0
for i in range(4):
    if gear[i][0] == 1:
        result += 2 ** i

print(result)