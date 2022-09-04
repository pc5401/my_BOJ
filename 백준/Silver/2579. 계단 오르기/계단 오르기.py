N = int(input()) # 0~300
lst = [int(input()) for _ in range(N)]

dp = [0] * N
stage = [0]*N

if N < 3:
    print(sum(lst))
    exit()

dp[0] = lst[0]
dp[1] = lst[1] + dp[0]
dp[2] = lst[2] + max(dp[0],lst[1])

for i in range(3,N):
    dp[i] = lst[i] + max(dp[i-3] + lst[i-1], dp[i-2])

print(dp[N-1])