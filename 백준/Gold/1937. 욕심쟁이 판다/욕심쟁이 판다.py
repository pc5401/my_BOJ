import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x,y):
    global N
    
    if dp[x][y] == 0: # 미탐색
        dp[x][y] = 1 # 탐색됨

        for d  in [[1,0],[-1,0],[0,-1],[0,1]]:
            ni = x + d[0]
            nj = y + d[1]

            if 0 <= ni < N and 0 <= nj < N and arr[x][y] < arr[ni][nj]: #범위 + 대나무 많이
                dp[x][y] = max(dfs(ni,nj)+1,dp[x][y])

    return dp[x][y]


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
maxV = 0

for i in range(N):
    for j in range(N):
        if dp[i][j]:
            continue
        value = dfs(i,j)
        maxV = max(maxV,value)
# print(dp)
print(maxV)