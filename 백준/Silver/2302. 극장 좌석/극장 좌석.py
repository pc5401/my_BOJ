from collections import deque, defaultdict
import sys
input = sys.stdin.readline


N = int(input())
dp = [1] * (N+1)
M = int(input())


for i in range(M):
    v = int(input())
    dp[v] = -1
    if v+1 <= N:
        dp[v+1] = -1 
    
if N == 1:
    print(1)
    quit()


for i in range(2,N+1):
    if dp[i] == -1:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[N] if dp[N] > 0 else abs(dp[N]))