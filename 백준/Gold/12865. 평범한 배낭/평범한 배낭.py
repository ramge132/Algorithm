n, k = map(int, input().split())

items = [tuple(map(int, input().split())) for _ in range(n)]


weight = [0] * (k + 1)

for w, v in items:
    for i in range(k, w-1, -1):
        weight[i] = max(weight[i], weight[i - w] + v)

print(weight[k])
