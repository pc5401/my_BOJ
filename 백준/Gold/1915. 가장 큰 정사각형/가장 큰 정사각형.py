import sys
input = sys.stdin.readline

def res(n:int,m:int):
    dp = [[0] * (m+1) for i in range(n+1)]
    res = 0
    for i in range(1,n+1):
        for j in range(1,m+1):

            if arr[i-1][j-1]:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
                res = max(res, dp[i][j]*dp[i][j])

    return res


if __name__ == "__main__":
    a,b = map(int,input().split())
    arr = [list(map(int,input().rstrip())) for _ in range(a)]
    
    print(res(a,b))
