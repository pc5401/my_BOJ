import sys
input = sys.stdin.readline

def stack_book(n: int, m: int, lst: list):

    stack = 0
    res = 1
    for i in lst:
        if stack + i > m:
            stack = i
            res += 1
        else:
            stack += i

    return res

if __name__ == "__main__":
    N, M = map(int,input().split())
    if N > 0 :
        lst = list(map(int,input().split()))
        print(stack_book(N, M, lst))
    else:
        print(0)