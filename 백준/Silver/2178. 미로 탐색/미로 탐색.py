from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for n in range(N)]

q = deque()
q.append([0, 0])

while q:
    v = q.popleft()

    for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        ni = v[0] + d[0]
        nj = v[1] + d[1]

        if 0 <= ni < N and 0 <= nj < M:
            if ni == N and nj == M:
                graph[ni][nj] = graph[v[0]][v[1]]

            elif graph[ni][nj] == 1:
                graph[ni][nj] = graph[v[0]][v[1]] + 1
                q.append([ni, nj])

print(graph[N-1][M-1])