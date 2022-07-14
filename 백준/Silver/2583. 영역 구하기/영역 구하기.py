from collections import deque

def bfs(i, j):
    global M, N
    ans = 0

    Q = deque()
    Q.append([i, j])

    while Q:

        v = Q.popleft()
        ans += 1
        for d in [[0,0],[-1,0], [1,0], [0,-1], [0,1]]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]
            if 0 <= ni < M and 0 <= nj < N:
                if arr[ni][nj] == 0:
                    Q.append([ni, nj])
                    arr[ni][nj] = 1

    return ans -1


M,N,K = map(int, input().split())
arr = [[0]*N for _ in range(M)]

for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

cnt = 0
res = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            cnt += 1
            res.append(bfs(i, j))

print(cnt)
res = sorted(res)
print(*res)