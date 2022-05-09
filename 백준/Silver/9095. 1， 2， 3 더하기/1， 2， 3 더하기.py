T = int(input())
dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):  # 11 보다 작음
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]


for tc in range(1, T+1):
    n = int(input())
    print(dp[n])