import sys
input = sys.stdin.readline

def solve(N: int, M: int, apples: list[int]) -> int:
    maxL = N - M + 1
    INF = 10**18
    dp = [INF] * (maxL + 1)
    dp[1] = 0  # 첨에는 L = 1

    for x in apples:
        new_dp = [INF] * (maxL + 1)
        lo = max(1, x - M + 1)
        hi = min(x, maxL)
        for L in range(1, maxL + 1):
            if dp[L] == INF:
                continue
            for newL in range(lo, hi + 1):
                cost = dp[L] + abs(newL - L)
                if cost < new_dp[newL]:
                    new_dp[newL] = cost
        dp = new_dp

    return min(dp[1:])

def main():
    # 입력
    N, M = map(int, input().split())
    J = int(input().strip())
    apples = [int(input().strip()) for _ in range(J)]
    # 풀이
    result = solve(N, M, apples)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
