import sys
import math
input = sys.stdin.readline

if __name__ == "__main__":
    dp = [1 for _ in range(1_000_000 + 1)]
    for i in range(1,1_000_000 + 1):
        dp[i] = (dp[math.floor(i-math.sqrt(i))] + dp[math.floor(math.log(i))] + dp[math.floor(i*math.sin(i)*math.sin(i))]) % 1000000
    
    while True:
        N = int(input())
        if N == -1:
            break
        else:
            print(dp[N])
