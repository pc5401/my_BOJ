from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

box = [[list(map(int, input().split())) for n in range(N)] for h in range(H)]

Q = deque()

zero = True

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                Q.append([h, n, m])
            elif box[h][n][m] == 0 and zero == True:  # 토마토가 없는 경우
                zero = False

if zero == True:
    print(0)
    quit()

while Q:

    v = Q.popleft()

    for d in [[0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1], [-1, 0, 0], [1, 0, 0]]:
        nh = v[0] + d[0]
        ni = v[1] + d[1]
        nj = v[2] + d[2]

        if 0 <= ni < N and 0 <= nj < M and 0 <= nh < H:
            if box[nh][ni][nj] == 0:
                box[nh][ni][nj] = box[v[0]][v[1]][v[2]] + 1
                Q.append([nh, ni, nj])

res = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] > res:
                res = box[h][n][m]
            elif box[h][n][m] == 0:
                print(-1)
                quit()

print(res-1)