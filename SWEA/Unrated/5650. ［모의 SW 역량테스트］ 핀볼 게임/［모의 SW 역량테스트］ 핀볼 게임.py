# 방향 정의
dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]

# 블록에 부딪혔을 때 방향 전환 정의
change_dir = [
    {},  # 빈 값 (사용하지 않음)
    {0: 1, 1: 3, 2: 0, 3: 2},  # 블록 1의 방향 전환
    {0: 3, 1: 0, 2: 1, 3: 2},  # 블록 2의 방향 전환
    {0: 2, 1: 0, 2: 3, 3: 1},  # 블록 3의 방향 전환
    {0: 1, 1: 2, 2: 3, 3: 0},  # 블록 4의 방향 전환
    {0: 1, 1: 0, 2: 3, 3: 2}  # 블록 5의 방향 전환 (벽과 동일)
]


def pinball(x, y, d, dxy, change_dir, hole):
    """
    핀볼을 움직이며 게임을 시뮬레이션하는 함수

    x, y : 핀볼의 현재 위치
    n : 게임판의 크기
    d : 핀볼의 현재 방향
    dxy : 방향 변화값
    change_dir : 블록에 부딪힐 때의 방향 전환 규칙
    hole : 웜홀의 위치 정보

    반환값 : 게임에서 얻은 점수
    """

    score = 0  # 게임 점수 초기화
    s_x, s_y = x, y  # 출발 위치 저장

    while True:
        # 핀볼을 현재 방향으로 한 칸 이동
        dx = x + dxy[d][0]
        dy = y + dxy[d][1]

        if maps[dy][dx] == -1:  # 블랙홀에 빠진 경우
            return score  # 게임 종료 후 점수 반환

        elif 1 <= maps[dy][dx] <= 5:  # 블록에 부딪힌 경우
            score += 1  # 점수 증가
            d = change_dir[maps[dy][dx]][d]  # 방향 전환
            x, y = dx, dy  # 위치 갱신

        elif 6 <= maps[dy][dx] <= 10:  # 웜홀을 만난 경우
            # 다른 위치의 웜홀로 이동
            for a, b in hole[maps[dy][dx]]:
                if (a, b) != (dx, dy):
                    x, y = a, b  # 웜홀 위치로 이동
                    break

        elif maps[dy][dx] == 0:  # 빈 공간인 경우
            x, y = dx, dy  # 핀볼 위치 갱신

        # 핀볼이 처음 위치로 돌아오면 게임 종료
        if (x, y) == (s_x, s_y):
            return score


T = int(input())

for t in range(1, T + 1):
    n = int(input())

    # 게임판의 외곽을 벽(5번 블록)으로 감싸줌
    maps = [[5] * (n + 2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(n)] + [[5] * (n + 2)]

    # 웜홀 위치 정보 저장
    hole = {i: [] for i in range(6, 11)}
    # 벽으로 감쌌기 때문에 range(1, n + 1)
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if 6 <= maps[y][x] <= 10:
                hole[maps[y][x]].append((x, y))

    # 가능한 모든 위치에서 최대 점수 계산
    max_score = 0
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if maps[y][x] == 0:  # 빈 공간에서만 출발 가능
                for d in range(4):  # 네 방향(상, 하, 좌, 우) 모두 시도
                    # dxy: 핀볼이 현재 방향 d로 움직일 때 x, y 좌표의 변화값
                    # dx, dy: 한 칸 이동했을 때 새로운 위치
                    dx = x + dxy[d][0]
                    dy = y + dxy[d][1]

                    # 다음 출발점이 빈 공간(0)이나 블랙홀(-1)일 경우, 해당 방향에서의 시뮬레이션을 건너뜀
                    if maps[dy][dx] <= 0:
                        continue

                    # 핀볼 시뮬레이션
                    score = pinball(x, y, d, dxy, change_dir, hole)
                    max_score = max(max_score, score)  # 최대 점수 갱신

    print(f'#{t} {max_score}')
