import sys
input = sys.stdin.readline


if __name__ == "__main__": # LIS DP 접근
    N = int(input())
    soldiers = list(map(int, input().split()))
    dp = [1] * N
    for i in range(1, N):
        for j in range(0, i):
            if soldiers[i] < soldiers[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[i] + 1
    
    print(N - max(dp))