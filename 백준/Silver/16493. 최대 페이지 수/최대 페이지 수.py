import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(M)]

dp = [[0] * (N+1) for _ in range(M+1)]

for i in range(1,M+1):
    for j in range(1,N+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-lst[i-1][0]] + lst[i-1][1]) if j-lst[i-1][0] >= 0 else dp[i-1][j]

print(dp[-1][-1])