def dfs(x, y):
    if not (0 <= x < n and 0 <= y < n) or visited[x][y] or matrix[x][y] == 0:
        return 0

    visited[x][y] = True

    count = 1

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        count += dfs(nx, ny)

    return count

n = int(input())

matrix = [list(map(int,input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

complex = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and not visited[i][j]:
            complex.append(dfs(i, j))

complex.sort()

print(len(complex))
for i in range(len(complex)):
    print(complex[i])