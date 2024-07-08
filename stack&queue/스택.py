from collections import deque

n = int(input())

stack = deque()

for _ in range(n):
    order = input()
    if 'push' in order:
        x = int(order.split(' ')[1])
        stack.append(x)

    elif order == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        print(int(len(stack) == 0))

    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
