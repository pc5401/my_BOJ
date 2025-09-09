import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

def solve(N, nxt):
    nxt = [0] + nxt
    vis = [0] * (N + 1)
    dp = [0] * (N + 1)

    def dfs(u):
        if vis[u]:
            return
        vis[u] = 1
        v = nxt[u]
        if not vis[v]:
            dfs(v)
        if vis[v] == 1:
            w = v
            cycle_len = 1
            while nxt[w] != v:
                w = nxt[w]
                cycle_len += 1
            w = v
            dp[w] = cycle_len
            vis[w] = 2
            while nxt[w] != v:
                w = nxt[w]
                dp[w] = cycle_len
                vis[w] = 2
        if vis[u] != 2:
            dp[u] = dp[v] + 1
            vis[u] = 2

    for i in range(1, N + 1):
        if not vis[i]:
            dfs(i)

    best_len = -1
    best_idx = 1
    for i in range(1, N + 1):
        if dp[i] > best_len or (dp[i] == best_len and i < best_idx):
            best_len = dp[i]
            best_idx = i
    return best_idx

def main():
    # 입력
    N = int(input().strip())
    nxt = [int(input().strip()) for _ in range(N)]

    # 풀이
    result = solve(N, nxt)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
