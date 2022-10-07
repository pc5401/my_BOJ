T = int(input())
dp = [[0,0] for _ in range(41)]
dp[0][0], dp[0][1] = 1, 0
dp[1][0], dp[1][1] = 0, 1
for d in range(2,41):
    dp[d][0] = dp[d-1][0] + dp[d-2][0]
    dp[d][1] = dp[d-1][1] + dp[d-2][1]

for tc in range(T):
    n = int(input())
    print(*dp[n])
