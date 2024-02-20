import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().split())
    space = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[0]*3 for j in range(M)] for _ in range(N) ]

    for j in range(M):
        dp[0][j][0], dp[0][j][1], dp[0][j][2] = space[0][j], space[0][j], space[0][j]

    for i in range(N):
        for j in range(M):
            for k in range(3):
                if (j == 0 and k == 0) or (j == M-1 and k == 2):
                    dp[i][j][k] = 1e9
                    continue

                if k == 0:
                    dp[i][j][k] = space[i][j] + min(dp[i-1][j-1][1], dp[i-1][j-1][2])
                elif k == 1:
                    dp[i][j][k] = space[i][j] + min(dp[i-1][j][0], dp[i-1][j][2])
                else:
                    dp[i][j][k] = space[i][j] + min(dp[i-1][j+1][0], dp[i-1][j+1][1])
    
    res = 1e9   
    for j in range(M):
        res = min(res, min(dp[N-1][j]))

    print(res)