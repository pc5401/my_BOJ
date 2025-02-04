import sys
input = sys.stdin.readline


def solve():
    dp = [0] * 68

    dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 4

    for n in range(4, 68):
        dp[n] = dp[n-1] + dp[n-2] + dp[n-3] + dp[n-4]
    
    return dp


def main():
    t = int(input())
    lst = [int(input()) for _ in range(t)]

    result = solve()

    for i in lst:
        print(result[i])

if __name__ == "__main__":
    main()
