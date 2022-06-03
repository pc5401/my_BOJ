from collections import deque

def bfs(i, j):
    
    que = deque()
    que.append([i,j])

    while que:

        v = que.popleft()

        for d in [[1,0], [-1, 0], [0, 1], [0, -1]]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]:
                que.append([ni, nj])
                arr[ni][nj] = 0


T = int(input())
for tc in range(T):
    M,N,K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for k in range(K):
        m, n = map(int,input().split())
        arr[n][m] = 1

    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                bfs(i,j)
                cnt += 1

    print(cnt)