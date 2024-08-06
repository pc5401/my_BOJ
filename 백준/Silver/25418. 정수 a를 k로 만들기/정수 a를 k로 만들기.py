import sys
input = sys.stdin.readline


def solve(A: int, K: int):
    dp = [1_000_001] * (K+1)
    dp[A] = 0
    for a in range(A, K):
        dp[a+1] = min(dp[a+1], dp[a] + 1)
        if a*2 <= K:
            dp[a*2] = min(dp[a*2], dp[a] + 1)

    return dp[K]

def main():
    A, K = map(int, input().split())
    print(solve(A, K))

main()

