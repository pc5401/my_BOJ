import sys
input = sys.stdin.readline

def bfs(i,j):
    global n, m

    visit[i][j] = 1
    q = [[i,j]]

    rtn = 0

    while q:
        rtn += 1
        v = q.pop()
        for d in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]
            if 0 <= ni < n and 0 <= nj < m and not visit[ni][nj] and graph[ni][nj]:
                visit[ni][nj] = 1
                q.append([ni,nj])

    return rtn


if __name__ == "__main__":
    n, m = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    cnt = 0
    res = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visit[i][j]:
                cnt += 1
                res = max(res, bfs(i,j))
            else:
                visit[i][j] = 1

    print(cnt)
    print(res)
