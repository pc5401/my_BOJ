import sys
from collections import deque
input = sys.stdin.readline

def solve(a: int, b: int, N: int, edges: list[tuple[int,int]]) -> int:
    adj = [[] for _ in range(N+1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    # BFS
    dist = [-1] * (N+1)
    q = deque([a])
    dist[a] = 0
    while q:
        u = q.popleft()
        if u == b:
            return dist[b]
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return -1

def main():
    # 입력
    a, b = map(int, input().split())
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    # 풀이
    result = solve(a, b, N, edges)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
