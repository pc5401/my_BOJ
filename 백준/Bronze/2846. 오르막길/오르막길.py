N = int(input())
lst = list(map(int,input().split()))
dp = [0] * N

for i in range(1,N):
    dp[i] = dp[i-1] + (lst[i] - lst[i-1]) if lst[i] > lst[i-1] else 0

print(max(dp))