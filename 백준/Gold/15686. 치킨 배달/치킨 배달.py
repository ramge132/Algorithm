from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

def get_city_chicken_distance(selected_chickens):
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in selected_chickens:
            distance = abs(hx - cx) + abs(hy- cy)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    return total_distance

min_chicken_distance = float('inf')
for selected_chickens in combinations(chickens, M):
    city_chicken_distance = get_city_chicken_distance(selected_chickens)
    min_chicken_distance = min(min_chicken_distance, city_chicken_distance)

print(min_chicken_distance)