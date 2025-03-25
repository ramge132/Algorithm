from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end = ' ')

    for next_node in graph[start]:
        if not visited[next_node]:
            dfs(graph, next_node, visited)

def bfs(graph, start):
    visited = [False] * (n + 1)
    visited[start] = True

    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for next_node in graph[v]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

dfs(graph, v, visited)
print()
bfs(graph, v)
