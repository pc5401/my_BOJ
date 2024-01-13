import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    triangle = [list(map(int,input().split())) for _ in range(N)]
    dp = [[0]*i for i in range(1, N+1)]

    for j in range(N):
        dp[N-1][j] = triangle[N-1][j]

    for i in range(N-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])

    print(dp[0][0])