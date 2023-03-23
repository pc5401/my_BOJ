from collections import defaultdict
import sys
input = sys.stdin.readline


def x_y_change(i,j,dir): # 좌표 이동
    global N, M
    ni = i + delta[dir][0]
    nj = j + delta[dir][1]
    
    if 0 <= ni < N and  0 <= nj < M:
        return ni, nj, False
    else:
        return i, j, True
    
def dise_move(dir): # 주사위 변경
    b,t = dise[0], dise[5]
    e,w,n,s = dise[1], dise[2], dise[3], dise[4]
    new = [0,0,0,0,0,0,0]
    if dir == 1: # 동쪽
        new[0] = e
        new[1] = t
        new[2] = b
        new[3] = n
        new[4] = s
        new[5] = w
    elif dir == 2: # 서쪽
        new[0] = w
        new[1] = b
        new[2] = t
        new[3] = n
        new[4] = s
        new[5] = e
    elif dir == 3: # 북쪽
        new[0] = n
        new[1] = e
        new[2] = w
        new[3] = t
        new[4] = b
        new[5] = s
    elif dir == 4: # 남쪽
        new[0] = s
        new[1] = e
        new[2] = w
        new[3] = b
        new[4] = t
        new[5] = n

    return new


res = []
delta = [[0,0],[0,1],[0,-1],[-1,0],[1,0]] #  동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
dise = [1,3,4,2,5,6]
data = {1:0,2:0,3:0,4:0,5:0,6:0}

N,M,x,y,K = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
move = list(map(int,input().split()))

for m in move:
    x,y,z = x_y_change(x,y,m) # 좌표 이동
    if z: # 벽침?
        continue

    dise = dise_move(m)
    val = graph[x][y]
    if val: # 0이 아니면
        data[dise[0]] = val
        graph[x][y] = 0
    else:
        graph[x][y] = data[dise[0]]

    res.append(data[dise[5]])



for r in res:
    print(r)