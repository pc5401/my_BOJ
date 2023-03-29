from collections import deque
import sys
input = sys.stdin.readline

def bfs(i,j):
    global N, M
    
    lst = [[0] * M for _ in range(N)]
    q = deque()
    q.append([i,j])
    lst[i][j] = 1

    while q:

        ii,jj = q.popleft()
        for d in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni = d[0] + ii
            nj = d[1] + jj
            if 0 <= ni < N and 0 <= nj < M and not lst[ni][nj] and graph[ni][nj] == 'L':
                q.append([ni,nj])
                lst[ni][nj] = lst[ii][jj] + 1

    return lst[ii][jj] - 1


res = 0
N, M = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(N)]
arr = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L' and arr[i][j] == 0:
            v = bfs(i,j)
            res = max(res,v)

print(res)