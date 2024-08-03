from itertools import permutations

N, M = map(int, input().split())

numbers = list(range(1, N + 1))

sequences = permutations(numbers, M)

for sequence in sequences:
    print(' '.join(map(str, sequence)))

