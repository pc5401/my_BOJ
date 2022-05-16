import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for n in range(N)]
dp = [[0]*N for n in range(N)]

dp[0][0] = 1
for i in range(N):
    for j in range(N):
        num = arr[i][j]
        if num > 0:  # 0 == 이동 불가
            if 0 <= i + num < N:
                dp[i + num][j] += dp[i][j]

            if 0 <= j + num < N:
                dp[i][j + num] += dp[i][j]

print(dp[-1][-1])