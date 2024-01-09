import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    xy_list = [list(map(int,input().split())) for _ in range(M)]

    dp = [[0]*(N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

    for x1, y1, x2, y2 in xy_list:
        print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])