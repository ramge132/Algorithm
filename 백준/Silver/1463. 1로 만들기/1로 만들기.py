# https://www.acmicpc.net/problem/1463

def min_operations_to_one(N):
    # DP 테이블 초기화
    dp = [0] * (N + 1)
    
    for i in range(2, N + 1):
        # 현재 수에서 1을 빼는 경우
        dp[i] = dp[i - 1] + 1
        
        # 현재 수가 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        # 현재 수가 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[N]

N = int(input())
print(min_operations_to_one(N))
