import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())
J_point = [] # 지훈이 시작점
F_point = [] # 불 시작점
fld = []
arr = [[0] * C for _ in range(R)]

for i in range(R): # input 처리
    l = list(input())
    for j in range(C):
        if l[j] == 'J':
            arr[i][j] = 1
            J_point.append([1, i, j])
        elif l[j] == 'F':
            F_point.append([0, i, j])
            arr[i][j] = -1
            # print(i,j)

    fld.append(l[:C])
delta = [[0,1],[1,0],[-1,0],[0,-1]]
Q = deque()  # Q 세팅
if F_point:
    for f in F_point:
        Q.append(f)
Q.append(*J_point)

res = 0
cnt = 1 # 지훈이 숫자.
while Q:
    if res or cnt == 0:
        break

    v, i, j = Q.popleft()
    
    if v: # 지훈이
        # print(f'지훈이 {v} 번째 이동 좌표({i},{j})')
        cnt -= 1
        for d in delta:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < R and 0 <= nj < C:
                if arr[ni][nj] or fld[ni][nj] == '#': # 이미 왔던가, 불, 벽
                    continue
                elif fld[ni][nj]  == '.': # 갈 수 있어.
                    arr[ni][nj] = v+1
                    Q.append([v+1,ni,nj])
                    cnt += 1
            else: # 도착, 끝
                res = v
                break
    else: # 불
        # print(f'불 {v} 번째 이동 좌표({i},{j})')
        for d in delta:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < R and 0 <= nj < C:
                if arr[ni][nj] or fld[ni][nj] == '#': # 이미 왔던가, 불, 벽
                    continue
                elif fld[ni][nj]  == '.': # 갈 수 있어.
                    arr[ni][nj] = -1
                    Q.append([0,ni,nj])

# print(f'arr 값',arr)
if res:
    print(res)
else:
    print('IMPOSSIBLE')




