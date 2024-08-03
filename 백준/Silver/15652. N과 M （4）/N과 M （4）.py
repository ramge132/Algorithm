from itertools import combinations_with_replacement

N, M = map(int, input().split())

numbers = list(range(1, N + 1))

# combinations_with_replacement 함수를 사용하여 
# 비내림차순으로 길이 M인 수열 생성
sequences = combinations_with_replacement(numbers, M)

for sequence in sequences:
    print(' '.join(map(str, sequence)))