def func(n:int) -> int:
    dp = [0] * (n+1)

    for i in range(1,n+1):
        dp[i] = i # dp 초기값 세팅
        j = 1 # index 초기값

        while j*j <= i: 
            dp[i] = min(dp[i],dp[i-j*j] + 1)
            j += 1

    return dp[n]

if __name__ == "__main__":
    N = int(input())
    print(func(N))