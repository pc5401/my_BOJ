import sys
input = sys.stdin.readline


if __name__ == '__main__':
    T = int(input())
    n_lst = [int(input()) for _ in range(T)]
    dp = [1]*10001

    for n in range(2, 10001):
        dp[n] += dp[n-2]
    
    for n in range(3, 10001):
        dp[n] += dp[n-3]

    for n in n_lst:
        print(dp[n])