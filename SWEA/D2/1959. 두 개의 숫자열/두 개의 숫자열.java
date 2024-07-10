def max_dot_product(N, M, Ai, Bj):
    max_sum = float('-inf')
    
    # Make sure Ai is the shorter or equal length array
    if N > M:
        N, M = M, N
        Ai, Bj = Bj, Ai
    
    # Slide Ai over Bj and compute the dot product
    for i in range(M - N + 1):
        current_sum = 0
        for j in range(N):
            current_sum += Ai[j] * Bj[i + j]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Reading input
T = int(input().strip())
for t in range(1, T + 1):
    N, M = map(int, input().strip().split())
    Ai = list(map(int, input().strip().split()))
    Bj = list(map(int, input().strip().split()))
    
    result = max_dot_product(N, M, Ai, Bj)
    print(f'#{t} {result}')
