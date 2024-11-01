from collections import deque

test_case = int(input())

for _ in range(test_case):
    n, target = map(int, input().split())
    priorities = list(map(int, input().split()))
    queue = deque([(i, priority) for i, priority in enumerate(priorities)])

    count = 0

    while queue:
        current = queue.popleft()

        if any(current[1] < doc[1] for doc in queue):
            queue.append(current)
        else:
            count+=1
            if current[0] == target:
                print(count)
                break
