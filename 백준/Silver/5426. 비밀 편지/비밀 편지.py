import sys
input = sys.stdin.readline


def solve(N: int, W: str):
    if N == 1:
        return W
    
    n = 1
    for i in range(2, 101):
        if i*i == N:
            n = i

    rtn = ''
    for i in range(n-1, -1, -1):
        for j in range(i, N, n):
            rtn += W[j]
    
    return rtn


def main():
    T = int(input())
    words = [input().rstrip() for _ in range(T)]
    result = [ solve(len(word), word) for word in words]
    for res in result:
        print(res)

main()
