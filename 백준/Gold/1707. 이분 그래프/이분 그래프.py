import sys
from collections import deque
input = sys.stdin.readline

def solve(V, E, edges):
    adj = [[] for _ in range(V + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (V + 1)
    for s in range(1, V + 1):
        if color[s] != 0:
            continue
        color[s] = 1
        q = deque([s])
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = -cu
                    q.append(v)
                elif color[v] == cu:
                    return "NO"
    return "YES"

def main():
    # 입력
    K = int(input().strip())
    cases = []
    for _ in range(K):
        V, E = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(E)]
        cases.append((V, E, edges))

    # 풀이
    result = [solve(V, E, edges) for V, E, edges in cases]

    # 출력
    print("\n".join(result))

if __name__ == "__main__":
    main()
