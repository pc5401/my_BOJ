import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, adj, start):
    vis = [False] * (n + 1)
    q = deque([start])
    vis[start] = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not vis[v]:
                vis[v] = True
                q.append(v)
    return vis

def solve(n, m, edges):
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    for i in range(1, n + 1):
        adj[i].sort()
    vis = bfs(n, adj, 1)
    not_connected = [str(i) for i in range(1, n + 1) if not vis[i]]
    if not not_connected:
        return "0"
    return "\n".join(not_connected)

def main():
    # 입력
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    # 풀이
    ans = solve(N, M, edges)

    # 출력
    print(ans)

if __name__ == "__main__":
    main()
