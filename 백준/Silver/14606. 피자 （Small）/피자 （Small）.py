import sys
input = sys.stdin.readline

def main():
    N = int(input())
    dp = [0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    print(dp[N])

main()

