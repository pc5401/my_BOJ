import sys
input = sys.stdin.readline


def solve(n: int, lst: list):
    stack = []
    rtn = 0 

    for i, h in enumerate(lst):
        while stack and stack[-1][1] > h:
            j, v = stack.pop()
            width = i if not stack else i - stack[-1][0] - 1
            rtn = max(rtn, width*v)

        stack.append([i,h])

    while stack:
        j, v = stack.pop()
        width = n if not stack else n - stack[-1][0] - 1
        rtn = max(rtn, width*v)
    
    return rtn

if __name__ == '__main__':
    N = int(input())
    Arr = [ int(input()) for _ in range(N)]
    print(solve(N, Arr))