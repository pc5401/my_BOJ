import sys
input = sys.stdin.readline


if __name__ == '__main__':
    T = int(input())
    n_lst = [int(input()) for _ in range(T)]
    dp = [0]*10001
    dp[1], dp[2], dp[3] =1, 2, 3

    for n in range(10001):
        dp[n] = dp[n-3] + int(n/2) + 1
    
    for n in n_lst:
        print(dp[n])