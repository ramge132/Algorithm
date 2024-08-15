def is_valid(grid, x, y, direction, n):
    # direction에 따른 dx, dy 설정 (상, 하, 좌, 우)
    if direction == 0:  # 상
        dx, dy = -1, 0
    elif direction == 1:  # 하
        dx, dy = 1, 0
    elif direction == 2:  # 좌
        dx, dy = 0, -1
    elif direction == 3:  # 우
        dx, dy = 0, 1

    # 전선을 놓으려는 방향으로 진행하면서 확인
    nx, ny = x + dx, y + dy
    while 0 <= nx < n and 0 <= ny < n:
        if grid[nx][ny] != 0:
            return False
        nx += dx
        ny += dy
    return True

def place_wire(grid, x, y, direction, n):
    wire_length = 0
    if direction == 0:  # 상
        dx, dy = -1, 0
    elif direction == 1:  # 하
        dx, dy = 1, 0
    elif direction == 2:  # 좌
        dx, dy = 0, -1
    elif direction == 3:  # 우
        dx, dy = 0, 1

    nx, ny = x + dx, y + dy
    while 0 <= nx < n and 0 <= ny < n:
        grid[nx][ny] = 2  # 전선 설치
        wire_length += 1
        nx += dx
        ny += dy

    return wire_length

def remove_wire(grid, x, y, direction, n):
    if direction == 0:  # 상
        dx, dy = -1, 0
    elif direction == 1:  # 하
        dx, dy = 1, 0
    elif direction == 2:  # 좌
        dx, dy = 0, -1
    elif direction == 3:  # 우
        dx, dy = 0, 1

    nx, ny = x + dx, y + dy
    while 0 <= nx < n and 0 <= ny < n:
        grid[nx][ny] = 0  # 전선 제거
        nx += dx
        ny += dy

def backtrack(grid, cores, idx, connected, wire_sum, n):
    global max_connected, min_wire_length

    if idx == len(cores):
        if connected > max_connected or (connected == max_connected and wire_sum < min_wire_length):
            max_connected = connected
            min_wire_length = wire_sum
        return

    x, y = cores[idx]
    
    # 현재 Core를 연결하지 않는 경우
    backtrack(grid, cores, idx + 1, connected, wire_sum, n)

    # 네 방향으로 전선을 연결하는 경우
    for direction in range(4):
        if is_valid(grid, x, y, direction, n):
            wire_length = place_wire(grid, x, y, direction, n)
            backtrack(grid, cores, idx + 1, connected + 1, wire_sum + wire_length, n)
            remove_wire(grid, x, y, direction, n)

def solve(test_case, n, grid):
    cores = []
    
    # 코어 리스트 작성
    for i in range(1, n-1):
        for j in range(1, n-1):
            if grid[i][j] == 1:
                cores.append((i, j))
    
    global max_connected, min_wire_length
    max_connected = 0
    min_wire_length = float('inf')
    
    backtrack(grid, cores, 0, 0, 0, n)
    
    print(f'#{test_case} {min_wire_length}')

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    solve(t, n, grid)
