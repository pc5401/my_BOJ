from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

start = [0, 0, K]

Q = deque()
visited = [[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]

Q.append(start)
visited[start[0]][start[1]][start[2]] = 1

def bfs():
    global res
    while Q:
        v = Q.popleft()

        for d in [[-1,0], [1,0], [0,-1], [0,1]]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]
            if 0 <= ni < N and 0 <= nj < M:

                if ni == N-1 and nj == M-1:  # 목적지 도착
                    res = visited[v[0]][v[1]][v[2]]
                    return res + 1

                elif arr[ni][nj] and v[2] and not visited[ni][nj][v[2]-1]:  # 벽 and 뚫기 안 씀
                    Q.append([ni, nj, v[2] -1])
                    visited[ni][nj][v[2] -1] = visited[v[0]][v[1]][v[2]] + 1

                elif not arr[ni][nj] and not visited[ni][nj][v[2]]: # 걍 일반 길
                    Q.append([ni, nj, v[2]])
                    visited[ni][nj][v[2]] = visited[v[0]][v[1]][v[2]] + 1

        # print(visited)

    return -1

res = bfs()
print(1 if N==1 and M==1 else res)