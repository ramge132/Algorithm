from collections import deque

def josepus(N, K):
    queue = deque(range(1, N+1))
    result = []
    while queue:
        queue.rotate(-(K-1))
        result.append(queue.popleft())
    return result

N, K = map(int, input().split())
result = josepus(N, K)
print("<" + ", ".join(map(str, result)) + ">")
