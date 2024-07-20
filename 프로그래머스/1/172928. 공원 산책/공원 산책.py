def solution(park, routes):
    # 공원의 크기
    H = len(park)
    W = len(park[0])
    
    # 시작 지점 찾기
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                start_y, start_x = i, j
    
    # 방향 정의
    direction = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    
    # 현재 위치 초기화
    cur_y, cur_x = start_y, start_x
    
    for route in routes:
        op, n = route.split()
        n = int(n)
        dy, dx = direction[op]
        
        # 이동 가능한지 확인
        valid = True
        for step in range(1, n + 1):
            new_y = cur_y + dy * step
            new_x = cur_x + dx * step
            if new_y < 0 or new_y >= H or new_x < 0 or new_x >= W or park[new_y][new_x] == 'X':
                valid = False
                break
        
        # 이동 가능하면 위치 갱신
        if valid:
            cur_y += dy * n
            cur_x += dx * n
    
    return [cur_y, cur_x]