from collections import defaultdict,deque
import sys
input = sys.stdin.readline

delta = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
N,M,K = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(N)] # 양분
tree = defaultdict(list) # 나무 정보
for _ in range(M):
    x,y,z = map(int,input().split())
    x -= 1
    y -= 1
    tree[(x,y)].append(z)
arr = [[5]*N for n in range(N)]

for k in range(K):
    # spring
    for idx in tree:
        if tree[idx]:
            lst = tree[idx] # 정렬된 나무들
            yang = arr[idx[0]][idx[1]] # 현재 양분
            dead = 0
            cnt = 0
            lst.sort()
            for i,l in enumerate(lst):
                if yang >= l:
                    lst[i] += 1
                    yang -= l
                    cnt += l
                #summer
                else: # 죽은 나무
                    dead += 1
                    arr[idx[0]][idx[1]] += l // 2

            arr[idx[0]][idx[1]] -= cnt  # 양분 빼기
            for d in range(dead):
                tree[idx].pop() # 죽은 나무 제거
    # fall
    fall = []
    for idx in tree:
        if tree[idx]:
            lst = tree[idx]
            for l in lst:
                if l % 5 == 0:
                    fall.append(idx)
                    
    for idx in fall:
        for d in delta:
            ni = idx[0] + d[0]
            nj = idx[1] + d[1]
            if 0 <= ni < N and 0 <= nj < N:
                tree[(ni,nj)].append(1)
    #winter 
    for i in range(N):
        for j in range(N):
            arr[i][j] += A[i][j]
res = 0
for idx in tree:
    res += len(tree[idx])

print(res)