import sys
from collections import deque
input = sys.stdin.readline

def solve(N, edges):
    out = [[] for _ in range(N + 1)]
    indeg = [0] * (N + 1)
    for u in range(1, N + 1):
        a, b = edges[u - 1]
        out[u].append(a)
        out[u].append(b)
        indeg[a] += 1
        indeg[b] += 1

    removed = [False] * (N + 1)
    q = deque(i for i in range(1, N + 1) if indeg[i] < 2)

    while q:
        u = q.popleft()
        if removed[u]:
            continue
        removed[u] = True
        for v in out[u]:
            if removed[v]:
                continue
            indeg[v] -= 1
            if indeg[v] == 1:
                q.append(v)

    res = [i for i in range(1, N + 1) if not removed[i]]
    res.sort()
    return res

def main():
    # 입력
    N = int(input().strip())
    edges = [tuple(map(int, input().split())) for _ in range(N)]

    # 풀이
    kept = solve(N, edges)

    # 출력
    if not kept:
        print(0)
    else:
        print(len(kept))
        print(" ".join(map(str, kept)))

if __name__ == "__main__":
    main()
