import sys
input = sys.stdin.readline

def dp_solve(n:int) -> tuple:
    min_dp = [0] * 3
    max_dp = [0] * 3

    for i in range(n):
        a,b,c = map(int,input().split())
        min_dp[0], min_dp[1] ,min_dp[2] = min(min_dp[0], min_dp[1]) + a, min(min_dp[0], min_dp[1], min_dp[2]) + b, min(min_dp[1], min_dp[2]) + c
        max_dp[0], max_dp[1] ,max_dp[2] = max(max_dp[0], max_dp[1]) + a, max(max_dp[0], max_dp[1], max_dp[2]) + b, max(max_dp[1], max_dp[2]) + c

    return max(max_dp), min(min_dp)

if __name__ == "__main__":
    N = int(input())
    print(*dp_solve(N))

