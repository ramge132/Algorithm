def min_sugar_bags_dp(N):
    # DP 테이블 초기화
    dp = [float('inf')] * (N + 1)
    dp[0] = 0  # 0kg은 봉지 필요 없음
    
    # DP 계산
    for i in range(3, N + 1):
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + 1)
        if i >= 5:
            dp[i] = min(dp[i], dp[i - 5] + 1)
    
    # 결과 반환
    return dp[N] if dp[N] != float('inf') else -1

# 예제 입력
N = int(input())
print(min_sugar_bags_dp(N))
