import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    dp = [[1e9]*N for _ in range(N)]
    B = int(input())
    for b  in range(B):
        a, b, c = map(int,input().split())
        dp[a-1][b-1] = min(c, dp[a-1][b-1])

    for k in range(N):
        dp[k][k] = 0
        for i in range(N):
            for j in range(N):

                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]

    for i in range(N):
        for j in range(N):
            if dp[i][j] == 1e9:
                dp[i][j] = 0

    for d in range(N):
        print(*dp[d])