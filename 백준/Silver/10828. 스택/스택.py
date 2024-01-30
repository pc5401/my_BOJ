import sys
input = sys.stdin.readline


if __name__ == '__main__':
    stack = []
    res = []
    N = int(input())
    for _ in range(N):
        order = input().split()
        if order[0] == 'push':
            stack.append(order[1])
        elif order[0] == 'pop':
            res.append(stack.pop() if stack else -1)
        elif order[0] == 'size':
            res.append(len(stack))
        elif order[0] == 'empty':
            res.append(0 if stack else 1)
        elif order[0] == 'top':
            res.append(stack[-1] if stack else -1)

    for r in res:
        print(r)
