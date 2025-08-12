import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def solve(N, M, edges, Q, queries):
    name2id = {}
    def gid(x):
        if x not in name2id:
            name2id[x] = len(name2id)
        return name2id[x]

    for a, b in edges:
        gid(a); gid(b)
    for a, b in queries:
        gid(a); gid(b)

    V = len(name2id)
    adj = [[] for _ in range(V)]
    for a, b in edges:
        adj[name2id[a]].append(name2id[b])

    seen = [0] * V
    stamp = 0
    def reaches(u, v):
        nonlocal stamp
        if u == v:
            return True
        stamp += 1
        dq = deque([u])
        seen[u] = stamp
        while dq:
            x = dq.popleft()
            for y in adj[x]:
                if seen[y] == stamp:
                    continue
                if y == v:
                    return True
                seen[y] = stamp
                dq.append(y)
        return False

    out = []
    for a, b in queries:
        ia, ib = name2id[a], name2id[b]
        if a == b:
            out.append("gg")
            continue
        if reaches(ia, ib):
            out.append(a)
        elif reaches(ib, ia):
            out.append(b)
        else:
            out.append("gg")
    return out

def main():
    # 입력
    N, M = map(int, input().split())
    edges = [tuple(input().split()) for _ in range(M)]
    Q = int(input())
    queries = [tuple(input().split()) for _ in range(Q)]

    # 풀이
    result = solve(N, M, edges, Q, queries)

    # 출력
    print(" ".join(result))

if __name__ == "__main__":
    main()
