from itertools import permutations

# 사용자로부터 N과 M을 입력받습니다.
N, M = map(int, input().split())

# N개의 수를 입력받습니다.
numbers = list(map(int, input().split()))

# 입력받은 수를 정렬합니다.
numbers.sort()

# 순열을 저장할 집합을 초기화합니다.
unique_sequences = set()

# permutations 함수를 사용하여 모든 순열을 생성합니다.
for sequence in permutations(numbers, M):
    unique_sequences.add(sequence)

# 집합에 저장된 순열을 사전 순으로 정렬하여 출력합니다.
for sequence in sorted(unique_sequences):
    print(' '.join(map(str, sequence)))
