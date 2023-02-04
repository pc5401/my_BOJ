import sys
input = sys.stdin.readline

delta = [[0,1],[0,-1],[1,0],[-1,0]]

def first(data):
    global N
    lst = data[1:5] # 친구 리스트
    cnd = [] # 친구가 가장 많은 리스트
    maxV = 0
    cnt = 0

    for i in range(N):
        for j in range(N):
            if room[i][j]:
                continue
            cnt = 0
            for d in delta:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < N and 0 <= nj < N:
                    if room[ni][nj] in lst: # 친구 수 
                        cnt += 1
            if cnt > maxV:
                maxV = cnt
                cnd = []
                cnd.append([i,j])
            elif cnt == maxV:
                cnd.append([i,j])
    l = len(cnd)

    if l == 1: # 좌표값 x, y 
        return cnd[0][0], cnd[0][1]
    else:
        return second(cnd)

def second(cnd:list): # 비어있는 칸이 가장 많이 있는지.
    global N

    maxVV = 0
    bin_max_lst = []
    for c in cnd:
        cntt = 0
        for d in delta:
            ni = c[0] + d[0]
            nj = c[1] + d[1]
            if 0 <= ni < N and 0 <= nj <N and room[ni][nj] == 0:
                cntt += 1
        if cntt > maxVV:
            maxVV = cntt
            bin_max_lst = []
            bin_max_lst.append(c)
        elif cntt == maxVV:
            bin_max_lst.append(c)

    bin_l = len(bin_max_lst)
    if bin_l == 1:
        return bin_max_lst[0][0], bin_max_lst[0][1]
    else:
        return third(bin_max_lst)

def third(v_lst:list):
    v_lst.sort(key=lambda x:(x[0],x[1]))
    return v_lst[0][0], v_lst[0][1]



# 입력 받기
N = int(input())
f_lst = dict()
room = [[0]*N for _ in range(N)]
for n in range(N*N):
    data = list(map(int,input().split()))
    f_lst[data[0]] = data[1:5]
    r,c = first(data)
    room[r][c] = data[0]

res = 0
val = {0:0, 1:1, 2:10, 3:100, 4:1000}

for i in range(N):
    for j in range(N):
        cnt = 0
        v = room[i][j]
        fs = f_lst[v]
        for d in delta:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < N and 0 <= nj < N and room[ni][nj] in fs:
                cnt += 1
        res += val[cnt]
        

print(res)


