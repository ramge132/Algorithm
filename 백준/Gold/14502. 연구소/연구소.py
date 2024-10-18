from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def spread_virus(temp_lab):
    queue = deque()
    for i in range(N):
        for j in range(M):
            if temp_lab[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ny, nx = x + dxy[i][0], y + dxy[i][1]
            if 0 <= nx < M and 0 <= ny < N and temp_lab[ny][nx] == 0:
                temp_lab[ny][nx] = 2
                queue.append((ny, nx))

def get_safe_area(temp_lab):
    safe_area = 0
    for i in range(N):
        for j in range(M):
            if temp_lab[i][j] == 0:
                safe_area += 1
    return safe_area

empty_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]

max_safe_area = 0

for walls in combinations(empty_spaces, 3):
    temp_lab = copy.deepcopy(lab)

    for x, y in walls:
        temp_lab[x][y] = 1

    spread_virus(temp_lab)

    safe_area = get_safe_area(temp_lab)
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)

