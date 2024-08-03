from itertools import combinations_with_replacement

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

# combinations_with_replacement 함수를 사용하여 중복을 허용하여 
# 길이 M인 비내림차순 수열 생성
sequences = combinations_with_replacement(numbers, M)

for sequence in sequences:
    print(' '.join(map(str, sequence)))
