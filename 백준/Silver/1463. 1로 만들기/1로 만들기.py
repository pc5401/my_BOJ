import sys
input = sys.stdin.readline

N = int(input())
dp = [0] *(N+1)

dp[0] = N
if N >= 2 :dp[2] = 1
if N >= 3 :dp[3] = 1
if N >= 4:
    for i in range(4,N+1):
        a = i // 3 if i % 3 == 0 else 0
        b = i // 2 if i % 2  == 0 else 0
        dp[i] = min(dp[i-1], dp[a], dp[b]) + 1

print(dp[N])