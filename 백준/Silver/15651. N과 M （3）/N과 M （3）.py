from itertools import product

# 사용자로부터 N과 M을 입력받습니다.
N, M = map(int, input().split())

# 1부터 N까지의 숫자 리스트 생성
numbers = list(range(1, N + 1))

# product 함수를 사용하여 중복 허용, 길이 M인 수열 생성
sequences = product(numbers, repeat=M)

# 각 수열을 출력
for sequence in sequences:
    print(' '.join(map(str, sequence)))
