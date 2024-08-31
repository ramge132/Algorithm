def max_stair_score(stairs):
    n = len(stairs)
    if n == 1:
        return stairs[0]
    
    # DP 테이블 초기화
    max_score = [0] * n
    
    # 초기값 설정
    max_score[0] = stairs[0]
    if n > 1:
        max_score[1] = stairs[0] + stairs[1]
    if n > 2:
        max_score[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    
    # DP 계산
    for i in range(3, n):
        max_score[i] = max(max_score[i-2] + stairs[i], max_score[i-3] + stairs[i-1] + stairs[i])
    
    return max_score[-1]

n = int(input())
stairs = [int(input()) for _ in range(n)]
print(max_stair_score(stairs))
