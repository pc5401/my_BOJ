N, K = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(K + 1)]

for n in range(N + 1):
    dp[1][n] = 1

for k in range(2, K + 1):
    for n in range(N + 1):
        for i in range(n + 1):
            dp[k][n] += dp[k - 1][i]
        dp[k][n] %= 1000000000

print(dp[K][N])