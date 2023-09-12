import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    wall = [list(map(int, input().split())) for _ in range(N)]

    dp = [[[0 for k in range(3)] for j in range(N)] for i in range(N)] # 0가로 , 1 대각선,2 세로
    dp[0][1][0] = 1

    for i in range(N):
        for j in range(1, N):
            if dp[i][j][0]: # 가로
                if i+1 < N and j+1 < N and not wall[i+1][j+1] and not wall[i+1][j] and not wall[i][j+1]: # 대각선
                    dp[i+1][j+1][1] += dp[i][j][0]
                if j+1 < N and not wall[i][j+1]:
                    dp[i][j+1][0] += dp[i][j][0]
                    

            if dp[i][j][1]: # 대각선
                if i+1 < N and j+1 < N and not wall[i+1][j+1] and not wall[i+1][j] and not wall[i][j+1]:
                    dp[i+1][j+1][1] += dp[i][j][1]
                if i+1 < N and not wall[i+1][j]:
                    dp[i+1][j][2] += dp[i][j][1]
                if  j+1 < N and not wall[i][j+1]:
                    dp[i][j+1][0] += dp[i][j][1]

            if dp[i][j][2]: # 세로
                if i+1 < N and j+1 < N and not wall[i+1][j+1] and not wall[i+1][j] and not wall[i][j+1]:
                    dp[i+1][j+1][1] += dp[i][j][2]
                if i+1 < N and not wall[i+1][j]:
                    dp[i+1][j][2] += dp[i][j][2]

    print(sum(dp[-1][-1]))