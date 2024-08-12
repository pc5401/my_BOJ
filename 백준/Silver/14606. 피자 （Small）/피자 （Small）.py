import sys
input = sys.stdin.readline


def solve(N: int):
    dp = [0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    return dp[N]


def main():
    N = int(input())
    print(solve(N))

main()
