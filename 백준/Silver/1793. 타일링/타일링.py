import sys

def update_dp(n:int, v:int):
    for i in range(v,n+1):
        dp[i] = dp[i-1] + 2 * dp[i-2]
    return n + 1

if __name__ == "__main__":
    dp = [0] * 251
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3
    v = 3
    for line in sys.stdin:
        n = int(line)
        if dp[n]:
            print(dp[n])
        else:
            v = update_dp(n,v)
            print(dp[n])