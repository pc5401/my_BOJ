import sys
from fractions import Fraction
from math import gcd

def solve(N, edges):
    adj = [[] for _ in range(N)]
    for a, b, p, q in edges:
        adj[a].append((b, q, p))
        adj[b].append((a, p, q))
    r = [Fraction(0, 1) for _ in range(N)]
    visited = [False] * N
    from collections import deque
    dq = deque([0])
    r[0] = Fraction(1, 1)
    visited[0] = True
    while dq:
        u = dq.popleft()
        for v, m_num, m_den in adj[u]:
            if not visited[v]:
                r[v] = r[u] * Fraction(m_num, m_den)
                visited[v] = True
                dq.append(v)
    L = 1
    for f in r:
        L = L * f.denominator // gcd(L, f.denominator)
    xs = [f.numerator * (L // f.denominator) for f in r]
    G = 0
    for x in xs:
        G = gcd(G, x)
    return [x // G for x in xs]

def main():
    # 입력
    input = sys.stdin.readline
    N = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(N-1)]
    # 풀이
    result = solve(N, edges)
    # 출력
    print(*result)

if __name__ == "__main__":
    main()
