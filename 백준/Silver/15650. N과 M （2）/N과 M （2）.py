def backtrack(start, sequence, N, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(start, N + 1):
        sequence.append(i)
        backtrack(i + 1, sequence, N, M)
        sequence.pop()

N, M = map(int, input().split())

backtrack(1, [], N, M)
