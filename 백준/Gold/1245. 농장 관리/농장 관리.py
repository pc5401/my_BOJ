import sys
import collections
input = sys.stdin.readline


def bfs(N:int, M: int, i: int, j: int) -> int:
    value = lst[i][j]
    Q = collections.deque()
    Q.append((i,j))
    flag = 1

    while Q:
        v = Q.popleft()
        for d in [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]
            if 0 <= ni < N and 0 <= nj < M:
                if lst[ni][nj] == value and not visited[ni][nj]:
                    Q.append((ni, nj))
                    visited[ni][nj] = 1
                elif lst[ni][nj] > value:
                    flag = 0
    
    return 1 if flag else 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    lst = [ list(map(int,input().split())) for _ in range(N) ]
    result = 0
    visited = [ [0]*M for _ in range(N) ]

    for i in range(N):
        for j in range(M):
            if lst[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                result += bfs(N, M, i, j)
                # print(result, i, j)
                # for v in visited:
                #     print(v)

    print(result)