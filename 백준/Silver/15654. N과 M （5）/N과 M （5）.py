def backtrack(sequence, visited, numbers, N, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            sequence.append(numbers[i])
            backtrack(sequence, visited, numbers, N, M)
            sequence.pop()
            visited[i] = False

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

visited = [False] * N

backtrack([], visited, numbers, N, M)
