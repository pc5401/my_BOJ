from collections import deque

m, n = map(int, input().split())
arr = []
Que = deque([])

for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        if lst[j] == 1:
            Que.append([i, j])

    arr.append(lst)


def BFS():
    maxV = 0
    while Que:

        v = Que.popleft()
        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni = v[0] + d[0]  # y좌표
            nj = v[1] + d[1]  # x좌표

            if 0 <= ni < n and 0 <= nj < m:  # 범위를 벗어나지 않았을 경우
                if arr[ni][nj] == 0:  # and [ni, nj] not in visited:
                    Que.append([ni, nj])
                    arr[ni][nj] = arr[v[0]][v[1]] + 1
                    maxV = max(maxV, arr[ni][nj])

    return maxV - 1

res = BFS()
res = res if res > 0 else 0  # 모두 익었을 때 or 벽에 막혀 하나도 안 섞었을 때.

zero_cnt = [i.count(0) for i in arr]  # 썩지 않은 토마토가 있을 경우
res = -1 if zero_cnt.count(0) < len(zero_cnt) else res


print(res)