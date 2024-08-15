def is_valid(board, x, y, direction, N):
    # 전선을 연결할 수 있는지 확인하는 함수
    dx, dy = direction
    nx, ny = x + dx, y + dy
    while 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] != 0:
            return False
        nx += dx
        ny += dy
    return True

def set_wire(board, x, y, direction, N, value):
    # 전선을 설치하거나 제거하는 함수
    dx, dy = direction
    nx, ny = x + dx, y + dy
    length = 0
    while 0 <= nx < N and 0 <= ny < N:
        board[nx][ny] = value
        length += 1
        nx += dx
        ny += dy
    return length

def backtrack(board, cores, index, connected, wire_length, max_cores, min_wire_length, N):
    if index == len(cores):
        # 모든 Core에 대해 탐색을 마친 경우
        if connected > max_cores[0] or (connected == max_cores[0] and wire_length < min_wire_length[0]):
            max_cores[0] = connected
            min_wire_length[0] = wire_length
        return

    x, y = cores[index]
    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if is_valid(board, x, y, direction, N):
            length = set_wire(board, x, y, direction, N, 2)
            backtrack(board, cores, index + 1, connected + 1, wire_length + length, max_cores, min_wire_length, N)
            set_wire(board, x, y, direction, N, 0)
    
    # 현재 Core를 연결하지 않고 다음으로 넘어가는 경우
    backtrack(board, cores, index + 1, connected, wire_length, max_cores, min_wire_length, N)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    cores = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if board[i][j] == 1:
                cores.append((i, j))
    
    max_cores = [0]
    min_wire_length = [float('inf')]
    backtrack(board, cores, 0, 0, 0, max_cores, min_wire_length, N)
    
    print(f"#{test_case} {min_wire_length[0]}")
