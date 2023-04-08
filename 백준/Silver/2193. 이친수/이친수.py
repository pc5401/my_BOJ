N = int(input())
dp = [1] * (91)
for i in range(3,91):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N])