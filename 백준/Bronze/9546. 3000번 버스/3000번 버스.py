import sys
input = sys.stdin.readline


def main():
    T = int(input())
    lst = [int(input()) for _ in range(T)]
    dp = [0] * 31
    for i in range(30):
        dp[i+1] = dp[i] + 2**i

    result = [dp[k] for k in lst]
    for res in result:
        print(res)

main()