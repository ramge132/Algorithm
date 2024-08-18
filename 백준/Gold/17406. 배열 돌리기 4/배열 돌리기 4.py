import sys
from itertools import permutations
import copy

def rotate(matrix, r, c, s):
    # 시계 방향으로 회전시키기
    for layer in range(1, s+1):
        top_left = matrix[r-layer][c-layer]
        
        # 좌측 열 위로 이동
        for i in range(r-layer, r+layer):
            matrix[i][c-layer] = matrix[i+1][c-layer]
        
        # 하단 행 좌로 이동
        for i in range(c-layer, c+layer):
            matrix[r+layer][i] = matrix[r+layer][i+1]
        
        # 우측 열 아래로 이동
        for i in range(r+layer, r-layer, -1):
            matrix[i][c+layer] = matrix[i-1][c+layer]
        
        # 상단 행 우로 이동
        for i in range(c+layer, c-layer+1, -1):
            matrix[r-layer][i] = matrix[r-layer][i-1]
        
        matrix[r-layer][c-layer+1] = top_left

def calculate_value(matrix):
    return min(sum(row) for row in matrix)

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    K = int(data[2])
    
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, data[3 + i*M: 3 + (i+1)*M])))
    
    rotations = []
    for i in range(K):
        r = int(data[3 + N*M + 3*i]) - 1
        c = int(data[3 + N*M + 3*i + 1]) - 1
        s = int(data[3 + N*M + 3*i + 2])
        rotations.append((r, c, s))
    
    min_value = sys.maxsize
    
    for perm in permutations(rotations):
        new_matrix = copy.deepcopy(matrix)
        for r, c, s in perm:
            rotate(new_matrix, r, c, s)
        min_value = min(min_value, calculate_value(new_matrix))
    
    print(min_value)

if __name__ == "__main__":
    main()
