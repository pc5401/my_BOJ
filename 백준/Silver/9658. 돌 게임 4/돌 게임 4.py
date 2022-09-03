N = int(input())
dp = [1] * 1001

dp[1] = 0
dp[2] = 1
dp[3] = 0

for i in range(7, 1001):
    if dp[i-1] == dp[i-3] == dp[i-4] == 1:
        dp[i] = 0

res = 'SK' if dp[N] else 'CY'
print(res)