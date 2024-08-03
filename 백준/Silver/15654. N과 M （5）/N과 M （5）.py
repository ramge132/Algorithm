from itertools import permutations

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

sequences = permutations(numbers, M)

for sequence in sorted(sequences):
    print(' '.join(map(str, sequence)))