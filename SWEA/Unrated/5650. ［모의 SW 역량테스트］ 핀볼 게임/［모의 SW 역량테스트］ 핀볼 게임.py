# 이전 코드와 동일한 방향과 블록 방향 전환 정의
delta = [[0, -1], [0, 1], [-1, 0], [1, 0]]
change_dir = [
    {},
    {0: 1, 1: 3, 2: 0, 3: 2},
    {0: 3, 1: 0, 2: 1, 3: 2},
    {0: 2, 1: 0, 2: 3, 3: 1},
    {0: 1, 1: 2, 2: 3, 3: 0},
    {0: 1, 1: 0, 2: 3, 3: 2}
]

def moving_ball(x, y, n, d, delta, change_dir, hole):
    score = 0
    s_x, s_y = x, y
    visited = set()  # 방문한 경로를 기록

    while (x, y, d) not in visited:
        visited.add((x, y, d))  # 현재 경로 기록
        dx = x + delta[d][0]
        dy = y + delta[d][1]

        if maps[dy][dx] == -1:
            return score
        elif 1 <= maps[dy][dx] <= 5:
            score += 1
            d = change_dir[maps[dy][dx]][d]
            x, y = dx, dy
        elif 6 <= maps[dy][dx] <= 10:
            for a, b in hole[maps[dy][dx]]:
                if (a, b) != (dx, dy):
                    x, y = a, b
                    break
        elif maps[dy][dx] == 0:
            x, y = dx, dy

        if (x, y) == (s_x, s_y):
            return score
    
    return score  # 방문 경로 중복 발생 시 종료

def solve_pinball_game(n, maps):
    hole = {i: [] for i in range(6, 11)}
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if 6 <= maps[y][x] <= 10:
                hole[maps[y][x]].append((x, y))

    max_score = 0
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if maps[y][x] == 0:
                for d in range(4):
                    dx = x + delta[d][0]
                    dy = y + delta[d][1]
                    
                    if maps[dy][dx] > 0:
                        score = moving_ball(x, y, n, d, delta, change_dir, hole)
                        max_score = max(max_score, score)
    
    return max_score

# 입력 처리
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    maps = [[5] * (n + 2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(n)] + [[5] * (n + 2)]
    result = solve_pinball_game(n, maps)
    print(f'#{tc} {result}')
