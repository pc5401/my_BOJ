import sys
import collections
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().split())
    space = [list(map(int, input().split())) for _ in range(N)]
    Q = collections.deque()

    delta = (-1, 0, 1)
    for j in range(M):
        for d in range(3):
            nj = j + delta[d]
            if 0 <= nj < M:
                Q.append([1, nj, d, space[0][j]])

    res = 1e9
    while Q:
        i, j, prev, fuel = Q.popleft()
        if i == N:
            res = min(res, fuel)
            continue

        for d in range(3):
            nj = j + delta[d]
            if d != prev and 0 <= nj < M:
                Q.append([i+1, nj, d, fuel + space[i][j]])
        
    print(res)

