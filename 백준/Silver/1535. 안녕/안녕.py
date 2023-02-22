import sys
input = sys.stdin.readline
# 체력 = 100, 기쁨 = 0

N = int(input())
hp = list(map(int,input().split()))
delight = list(map(int,input().split()))

dp = [[0]*101 for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,101):
        if j - hp[i-1] > 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-hp[i-1]] + delight[i-1])
        else:
            dp[i][j] = dp[i-1][j]

# print(*dp, sep='\n')
print(dp[N][100])
