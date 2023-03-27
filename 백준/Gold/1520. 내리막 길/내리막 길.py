import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x,y):
    global N,M

    if x == N-1 and y == M-1:
        return 1
    
    if dp[x][y] == -1: # 미탐색
        dp[x][y] = 0 # 탐색됨

        for d  in [[1,0],[-1,0],[0,-1],[0,1]]:
            ni = x + d[0]
            nj = y + d[1]

            if 0 <= ni < N and 0 <= nj < M and arr[x][y] > arr[ni][nj]: #범위 + 내리막
                dp[x][y] += dfs(ni,nj)

    return dp[x][y]


N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1]*M for _ in range(N)]

print(dfs(0,0))