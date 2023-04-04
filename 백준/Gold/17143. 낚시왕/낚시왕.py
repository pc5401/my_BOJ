from collections import defaultdict
import sys
input = sys.stdin.readline

def fish(j):
    i = 0

    while R > i:
        v = graph[i][j]
        if v and sharks[v][4]:
            shark = sharks[v][4]
            sharks[v][4] = 0 # 크기가 영이면 잡힌 것
            graph[i][j] = 0
            return shark
        i += 1
    return 0

def battle(x,y): # y가 도전자
    if sharks[x][4] > sharks[y][4]:
        sharks[y][4] = 0 # y 상어 죽음
        return False
    else: 
        sharks[x][4] = 0 # x 상어 죽음
        return True

def move(j):
    global R,C,M
    arr = [[0]*C for i in range(R)]

    for m in range(1,M+1):
        if sharks[m][4] == 0: # 상어 즉음,
            continue
        r, c, s, d, z = sharks[m]
        ni, nj = r, c
        if d == 0 or d == 1:
            for i in range(s):
                ni += 1 * delta[d][0]
                if 0 <= ni < R:
                    continue
                d = 0 if d else 1
                ni += 2 * delta[d][0]
        else:
            for i in range(s):
                nj += 1 * delta[d][1]
                # print(f'o:{i}, nj:{nj}')
                if 0 <= nj < C:
                    continue
                d = 3 if d == 2 else 2
                nj += 2 * delta[d][1]

        p = arr[ni][nj]
        if p and p < m: # 이미 상어가 있다면,
            vs = battle(p,m)
            if vs:
                sharks[m][0],sharks[m][1],sharks[m][3] = ni,nj,d
                arr[ni][nj] = m
        else:
            sharks[m][0],sharks[m][1],sharks[m][3] = ni,nj,d
            arr[ni][nj] = m
    return arr


delta = [[-1,0],[1,0],[0,1],[0,-1]]
R,C,M  = map(int,input().split()) # M은 상어의 수
graph = [[0]*C for i in range(R)]
sharks = defaultdict(list)
for i in range(1,M+1):
    rr, cc, s, dd, z = map(int,input().split()) 
    r,c,d = rr-1,cc-1,dd-1 
    graph[r][c] = i
    sharks[i] = [r, c, s, d, z]
    # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기

res = 0
for j in range(C):
    res += fish(j) # 낚시
    graph = move(j)

print(res)
