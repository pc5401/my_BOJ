import sys
input = sys.stdin.readline


if __name__ == "__main__":
    P, N = map(int,input().split())
    res = 0
    dp = [0] * (N+1)
    dp[0] = P
    # 1년 5% 3년 20% 5년 35%
    for i in range(1,N+1):
        if i - 3 < 0:
            dp[i] = int(dp[i-1] * 1.05)
        elif i - 5 < 0:
            dp[i] = int(max(dp[i-1] * 1.05, dp[i-3] * 1.2))
        else:
            dp[i] = int(max(dp[i-1] * 1.05, dp[i-3] * 1.2, dp[i], dp[i-5] * 1.35))
    
    res = int(dp[N])
    print(res)
