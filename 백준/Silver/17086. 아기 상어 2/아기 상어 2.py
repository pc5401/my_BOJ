from collections import deque

delta =((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

Q = deque()
N, M = map(int, input().split())

arr = []
for n in range(N):
    lst = list(map(int, input().split()))
    for m in range(M):
        if lst[m] == 1:
            Q.append([n, m])  # Q에 입력
    arr.append(lst)

while Q:

    v = Q.popleft()

    for d in delta:
        ni = v[0] + d[0]
        nj = v[1] + d[1]

        if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]:
            Q.append([ni, nj])
            arr[ni][nj] = arr[v[0]][v[1]] + 1  # 방문 처리

res = 0
for l in arr:
    res = max(res, max(l))

print(res-1)