import sys
from collections import deque
input = sys.stdin.readline

def solve(n: int, k: int, adj: list[list[int]], val: list[int]) -> int:
    best = 0
    root_bit = 1 << 0
    for mask in range(1 << n):
        if not (mask & root_bit):
            continue

        apples = 0
        pears = 0
        for i in range(n):
            if mask & (1 << i):
                if val[i] == 1:
                    apples += 1
                elif val[i] == 2:
                    pears += 1
        if apples > k:
            continue
        # BFS
        visited = 0
        q = deque([0])
        visited |= 1 << 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if (mask & (1 << v)) and not (visited & (1 << v)):
                    visited |= 1 << v
                    q.append(v)
        if visited == mask:
            if pears > best:
                best = pears
    return best

def main():
    # 입력
    n, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        p, c = map(int, input().split())
        adj[p].append(c)
        adj[c].append(p)
    val = list(map(int, input().split()))
    # 풀이
    result = solve(n, k, adj, val)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
