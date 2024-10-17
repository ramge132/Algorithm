
stack = []

def push(num):
    stack.append(num)

def pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

N = int(input())

commands = [input().split() for _ in range(N)]

for command in commands:
    #print(f"stack:{stack}")
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'top':
        top()