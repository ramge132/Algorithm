from itertools import combinations

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

sequences = combinations(sorted(numbers), M)

for sequence in sequences:
    print(' '.join(map(str, sequence)))
