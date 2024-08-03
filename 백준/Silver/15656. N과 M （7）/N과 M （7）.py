from itertools import product

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

sequences = product(sorted(numbers), repeat=M)

for sequence in sequences:
    print(' '.join(map(str, sequence)))