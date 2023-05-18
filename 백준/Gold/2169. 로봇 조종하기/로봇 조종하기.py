import sys
input = sys.stdin.readline

def dp_solve(N:int, M:int):

    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1e9]*M for _ in range(N)]
    dp_left = [[-1e9]*M for _ in range(N)]
    dp_right = [[-1e9]*M for _ in range(N)]
    dp[0][0] = arr[0][0]
    for i in range(1,M): # 첫 줄
        dp[0][i] = dp[0][i-1] + arr[0][i]

    for i in range(1, N):
        if i > 0:
            for j in range(M):
                dp_left[i][j] = max(dp[i-1][j], dp_left[i][j-1]) + arr[i][j] if j > 0 else dp[i-1][j] + arr[i][j]
            for j in range(M-1, -1, -1):
                dp_right[i][j] = max(dp[i-1][j], dp_right[i][j+1]) + arr[i][j] if j + 1 < M else dp[i-1][j] + arr[i][j]
            for j in range(M):
                dp[i][j] = max(dp_left[i][j], dp_right[i][j])

    return dp[N-1][M-1]

if __name__ == "__main__":
    n, m = map(int,input().split())
    print(dp_solve(n,m))