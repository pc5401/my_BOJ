import itertools
from collections import deque
import copy

n, m = map(int, input().split())
wal = []  # 1, 벽
load = []  # 0, 길
vir = []  # 2, 바이러스
origin = []  # map
vir_que = deque() # 2, 바이러스

for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(m):
        if lst[j] == 1:
            wal.append([i, j])
        elif lst[j] == 2:
            vir.append([i, j])
        else:
            load.append([i, j])
    origin.append(lst)

maxV = -1
#  벽 3 개를 고르는 조합 생성
load_cmbn = list(map(list, itertools.combinations(load, 3)))  # 3차원 리스트!

for l in load_cmbn:
    arr = copy.deepcopy(origin)
    for cmbn in l:  # 벽 세우기
        arr[cmbn[0]][cmbn[1]] = 1

    # bfs
    for q in vir:
        vir_que.append(q)

    while vir_que:
        v = vir_que.popleft()

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  # 상하좌우
            ni = v[0] + di
            nj = v[1] + dj

            if 0 <= ni < n and 0 <= nj < m:  # 범위를 벗어나지 않고
                if not arr[ni][nj]:  # 0 이면, 바이러스 퍼짐
                    arr[ni][nj] = arr[v[0]][v[1]] + 1
                    vir_que.append([ni, nj])

    load_sum = [arr[c].count(0) for c in range(n)]
    maxV = max(maxV, sum(load_sum))

print(maxV)