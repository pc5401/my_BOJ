from collections import defaultdict, deque
dct = defaultdict(deque)
arr = []
# 입력처리

n, k = map(int, input().split())
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j] > 0:
            dct[lst[j]].append([i, j])
    arr.append(lst)

s, x, y = map(int, input().split())
x -= 1
y -= 1

keys = sorted(dct)
for ki in keys:
    dct[ki].append('flag')

result = 0
for cnt in range(s):
    for ki in keys:
        while 1:
            v = dct[ki].popleft()

            if v == 'flag':
                dct[ki].append('flag')
                break

            for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni = v[0] + d[0]
                nj = v[1] + d[1]

                if 0 <= ni < n and 0 <= nj < n:
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = arr[v[0]][v[1]]
                        dct[ki].append([ni, nj])

            if arr[x][y] != 0:
                result = arr[x][y]
                break
        if result != 0:
            result = arr[x][y]
            break
    if result != 0:
        result = arr[x][y]
        break

print(result)