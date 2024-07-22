
def n_pow_m(n, m):
    if m == 0:
        return 1
    elif m % 2 == 0:
        half = n_pow_m(n, m // 2)
        return half * half
    else:
        return n * n_pow_m(n, m - 1)

results = []

for _ in range(10):
    user_case = int(input())
    n, m = map(int, input().split())
    result = n_pow_m(n, m)
    results.append(f'#{user_case} {result}')

for result in results:
    print(result) 