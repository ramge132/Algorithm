def backtrack(depth, sequence):
    if depth == M:
        result.add(tuple(sequence))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            sequence.append(numbers[i])
            backtrack(depth + 1, sequence)
            sequence.pop()
            visited[i] = False

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

result = set()

visited = [False] * N

backtrack(0, [])

for sequence in sorted(result):
    print(' '.join(map(str, sequence)))
