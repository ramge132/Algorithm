import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if parents[neighbor] == 0:  # 아직 방문하지 않은 노드
                parents[neighbor] = node
                queue.append(neighbor)

# 입력 받기
N = int(input().strip())
tree = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)  # 각 노드의 부모를 저장할 리스트

# 트리의 간선 정보 입력받기
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# BFS로 부모 찾기 시작 (1번 노드를 루트로)
bfs()

# 2번 노드부터 N번 노드까지 부모 출력
for i in range(2, N + 1):
    print(parents[i])
