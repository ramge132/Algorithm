import math

test_case = int(input())

results = []

for _ in range(test_case):
    N, M = map(int, input().split())
    result = math.comb(M, N)
    results.append(result)
    
for res in results:
    print(res)