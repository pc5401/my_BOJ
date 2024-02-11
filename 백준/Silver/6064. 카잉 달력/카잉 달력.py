import sys
input = sys.stdin.readline


def foo(M: int, N: int, X: int, Y: int) -> int:
    if X == Y:
        return X
    
    x = X % M
    
    if x == 0:
        x = M
    
    for i in range(x, M*N+1, M): # x 고정 M의 배수만큼 증가
        if (i-Y) % N == 0:
            return i
    return -1

if __name__ == '__main__':
    res = []
    T = int(input())
    for _ in range(T):
        M, N, X, Y = map(int, input().split())
        res.append(foo(M, N, X, Y))

    for r in res:
        print(r)