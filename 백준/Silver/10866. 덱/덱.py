deque = []

def push_front(X):
    deque.insert(0, X)

def push_back(X):
    deque.append(X)

def pop_front():
    if deque:
        print(deque.pop(0))
    else:
        print(-1)

def pop_back():
    if deque:
        print(deque.pop())
    else:
        print(-1)

def size():
    print(len(deque))

def empty():
    if deque:
        print(0)
    else:
        print(1)

def front():
    if deque:
        print(deque[0])
    else:
        print(-1)

def back():
    if deque:
        print(deque[-1])
    else:
        print(-1)

N = int(input())

for _ in range(N):
    command = list(input().split())
    if command[0] == 'push_front':
        push_front(command[1])
    if command[0] == 'push_back':
        push_back(command[1])
    if command[0] == 'pop_front':
        pop_front()
    if command[0] == 'pop_back':
        pop_back()
    if command[0] == 'size':
        size()
    if command[0] == 'empty':
        empty()
    if command[0] == 'front':
        front()
    if command[0] == 'back':
        back()
