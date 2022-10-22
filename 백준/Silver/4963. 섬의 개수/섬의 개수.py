import sys
from collections import deque
input = sys.stdin.readline

def BFS(i,j):
    global w, h

    q = deque()
    q.append((i,j))

    while q:

        v = q.popleft()

        for d in [[0,-1], [0,1], [1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]
            if 0 <= ni < h and 0 <= nj < w and world[ni][nj]:
                world[ni][nj] = 0
                q.append((ni,nj))

res = []
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    world = [list(map(int, input().split()))for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if world[i][j]:
                world[i][j] = 0
                BFS(i,j)
                cnt += 1

    res.append(cnt)

for r in res:
    print(r)