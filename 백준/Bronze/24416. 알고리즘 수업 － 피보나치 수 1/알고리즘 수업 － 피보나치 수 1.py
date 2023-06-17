if __name__ == '__main__':
    N = int(input())
    dp = [0] * (N+1)
    dp[1], dp[2] = 1, 1
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    res = N - 2
    print(dp[N], res)
