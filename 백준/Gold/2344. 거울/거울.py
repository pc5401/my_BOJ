import sys
input = sys.stdin.readline


def func(lst):
    i, j = lst[0], lst[1]
    di, dj = lst[2], lst[3]
    ni, nj = di + i, dj + j
    while True:

        if 0 < ni < N+1 and 0 < nj < M+1:
            if arr[ni][nj]:
                d = delta[(di,dj)]
                di, dj = d[0], d[1]
                ni += d[0]
                nj += d[1]
                
            else:
                ni += di
                nj += dj

        else:
            return arr[ni][nj]


delta = {(0,1):[-1,0], (-1,0):[0,1], (0,-1):[1,0], (1, 0):[0,-1]}
N, M = map(int, input().split())
arr = [[-1] * (M +2)]
for m in range(N):
    arr.append([-1]+list(map(int, input().split()))+[-1])
arr.append([-1]*(M+2))
order = []
res = []

s = 1
for i in range(1, N+1):
    arr[i][0] = s
    s+= 1
    order.append([i,0,0,1])  # 0,1 은 좌표값 2,3 초기 진행 방향

for i in range(1, M+1):
    arr[N+1][i] = s
    s += 1
    order.append([N+1, i, -1, 0])

for i in range(N, 0, -1):
    arr[i][M+1] = s
    s += 1
    order.append([i, M+1, 0 , -1])

for i in range(M, 0, -1):
    arr[0][i] = s
    s += 1
    order.append([0, i, 1, 0])

for l in order:
    result = func(l)
    res.append(result)


print(*res)