import sys
from collections import deque
input = sys.stdin.readline

def solve(n: int, edges: list[tuple[int,int]]) -> bool:
    adj = [[] for _ in range(n+1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    color = [0] * (n+1)
    for start in range(1, n+1):
        if color[start] != 0:
            continue
        color[start] = 1
        dq = deque([start])
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = -color[u]
                    dq.append(v)
                elif color[v] == color[u]:
                    return False
    return True

def main():
    # 입력
    T = int(input().strip())
    for _ in range(T):
        n, m = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        # 풀이
        result = solve(n, edges)
        # 출력
        print("possible" if result else "impossible")

if __name__ == "__main__":
    main()
