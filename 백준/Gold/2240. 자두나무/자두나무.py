import sys

def solve(T, W, drops):
    INF_NEG = -10**9
    dp = [[INF_NEG]*(W+1) for _ in range(T+1)]
    dp[0][0] = 0
    for t in range(1, T+1):
        for m in range(0, W+1):
            best = dp[t-1][m]
            if m > 0:
                if dp[t-1][m-1] > best:
                    best = dp[t-1][m-1]
            pos = 1 if (m % 2 == 0) else 2
            dp[t][m] = best + (1 if drops[t-1] == pos else 0)
    return max(dp[T])

def main():
    #입력
    input = sys.stdin.readline
    T, W = map(int, input().split())
    drops = [int(input().strip()) for _ in range(T)]
    #풀이
    ans = solve(T, W, drops)
    #출력
    print(ans)

if __name__ == "__main__":
    main()
