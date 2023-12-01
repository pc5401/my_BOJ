import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    metrix = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    nums = [metrix[0][0]] + [met[1] for met in metrix] # 곱할 숫자 순서

    for l in range(2, N+1): # 길이
        for i in range(N - l + 1):
            j = i + l - 1 
            dp[i][j] = float('INF')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + nums[i] * nums[k + 1] * nums[j + 1]

                if cost < dp[i][j]:
                    dp[i][j] = cost

    print(dp[0][N-1])