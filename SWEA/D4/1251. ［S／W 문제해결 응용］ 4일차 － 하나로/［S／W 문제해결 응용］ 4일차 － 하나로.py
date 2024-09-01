import math
import heapq

class DisjointSet:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.p[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.p[rootX] = rootY
            else:
                self.p[rootY] = rootX
                self.rank[rootX] += 1

def calculate_distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def kruskal_mst(n, coords, e_rate):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_distance(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
            edges.append((dist, i, j))

    edges.sort() 
    ds = DisjointSet(n)
    total_cost = 0
    
    for dist, u, v in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            total_cost += dist
    
    return round(total_cost * e_rate)

T = int(input())  

for t in range(1, T + 1):
    n = int(input())  # 섬의 개수
    x_coords = list(map(int, input().split()))
    y_coords = list(map(int, input().split()))
    e_rate = float(input())  # 환경 부담 세율

    coords = [(x_coords[i], y_coords[i]) for i in range(n)]
    
    result = kruskal_mst(n, coords, e_rate)
    print(f"#{t} {result}")
