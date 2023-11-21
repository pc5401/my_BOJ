import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    dp = [[1e9]*N for _ in range(N)]
    while 1:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        dp[a-1][b-1] = 1
        dp[b-1][a-1] = 1

    for k in range(N):
        dp[k][k] = 0
        for i in range(N):
            for j in range(N):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    
    for i in range(N):
        for j in range(N):
            if dp[i][j] >= 1e9:
                dp[i][j] = 0
    
    ranks = [max(dp[i]) for i in range(N)]
    minV = min(ranks)
    res = []
    for i, rank in enumerate(ranks):
        if rank == minV:
            res.append(i+1)
    
    print(minV, len(res))
    print(*res)