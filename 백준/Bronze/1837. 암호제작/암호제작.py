def solution(p, k):
    for i in range(2, k):
        if p % i == 0:
            return f"BAD {i}"

    return "GOOD"

P, K = map(int,input().split())
print(solution(P, K))