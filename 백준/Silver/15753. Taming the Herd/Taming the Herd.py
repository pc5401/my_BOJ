import sys
input = sys.stdin.readline

def solve(N, log):
    dp = [[None]*(N+1) for _ in range(N+1)]
    if log[0] != -1 and log[0] != 0:
        return -1
    dp[1][0] = (1, 1)
    for day in range(2, N+1):
        for prev in range(N+1):
            if dp[day-1][prev] is None:
                continue
            if log[day-1] == -1 or log[day-1] == 0:
                cand = (dp[day-1][prev][0] + 1, dp[day-1][prev][1] + 1)
                if dp[day][0] is None:
                    dp[day][0] = cand
                else:
                    cur = dp[day][0]
                    dp[day][0] = (min(cur[0], cand[0]), max(cur[1], cand[1]))
            new_val = prev + 1
            if new_val <= N and (log[day-1] == -1 or log[day-1] == new_val):
                cand = dp[day-1][prev]
                if dp[day][new_val] is None:
                    dp[day][new_val] = cand
                else:
                    cur = dp[day][new_val]
                    dp[day][new_val] = (min(cur[0], cand[0]), max(cur[1], cand[1]))
    mn = 10**9
    mx = -1
    valid = False
    for j in range(N+1):
        if dp[N][j] is not None:
            valid = True
            mn = min(mn, dp[N][j][0])
            mx = max(mx, dp[N][j][1])
    if not valid:
        return -1
    return (mn, mx)

def main():
    N = int(input().strip())
    log = list(map(int, input().split()))
    result = solve(N, log)
    if result == -1:
        print(-1)
    else:
        print(result[0], result[1])

if __name__ == "__main__":
    main()
