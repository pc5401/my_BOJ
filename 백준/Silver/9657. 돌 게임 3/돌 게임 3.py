N = int(input())
dp = [1] * 1005

dp[2] = 0

for i in range(7, 1005):
    if dp[i-1] == dp[i-3] == dp[i-4] == 1:
        dp[i] = 0

res = 'SK' if dp[N] else 'CY'
print(res)