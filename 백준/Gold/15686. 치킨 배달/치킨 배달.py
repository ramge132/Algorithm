from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chicken_shops = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chicken_shops.append((r, c))

# 치킨 거리를 계산하는 함수
def get_chicken_distance(selected_chickens):
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in selected_chickens:
            distance = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    return total_distance

# 모든 치킨집 조합 중에서 최적의 조합을 탐색
min_distance = float('inf')
for chickens in combinations(chicken_shops, M):
    min_distance = min(min_distance, get_chicken_distance(chickens))

print(min_distance)
