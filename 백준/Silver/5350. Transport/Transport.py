import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N,W = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)] # w(무게),v(가치)
    
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, W+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-lst[i-1][0]] + lst[i-1][1]) if j-lst[i-1][0] >= 0 else dp[i-1][j]
    print(dp[N][W])

