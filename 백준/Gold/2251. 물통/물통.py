import sys
from collections import deque

input = sys.stdin.readline

def pour(from_amt, from_cap, to_amt, to_cap):
    t = min(from_amt, to_cap - to_amt)
    return from_amt - t, to_amt + t

def solve(A, B, C):
    total = C
    vis = [[False] * (B + 1) for _ in range(A + 1)]
    q = deque()
    ans = set()

    q.append((0, 0))
    vis[0][0] = True
    ans.add(C)  # 처음 상태에서 A가 비어 있고 C 가득

    while q:
        a, b = q.popleft()
        c = total - a - b

        # a -> b
        na, nb = pour(a, A, b, B)
        if not vis[na][nb]:
            vis[na][nb] = True
            q.append((na, nb))
            if na == 0:
                ans.add(total - na - nb)

        # a -> c
        na, nc = pour(a, A, c, C)
        nb = b
        if not vis[na][nb]:
            vis[na][nb] = True
            q.append((na, nb))
            if na == 0:
                ans.add(total - na - nb)

        # b -> a
        nb, na = pour(b, B, a, A)
        if not vis[na][nb]:
            vis[na][nb] = True
            q.append((na, nb))
            if na == 0:
                ans.add(total - na - nb)

        # b -> c
        nb, nc = pour(b, B, c, C)
        na = a
        if not vis[na][nb]:
            vis[na][nb] = True
            q.append((na, nb))
            if na == 0:
                ans.add(total - na - nb)

        # c -> a
        nc, na = pour(c, C, a, A)
        nb = b
        if not vis[na][nb]:
            vis[na][nb] = True
            q.append((na, nb))
            if na == 0:
                ans.add(total - na - nb)

        # c -> b
        nc, nb = pour(c, C, b, B)
        na = a
        if not vis[na][nb]:
            vis[na][nb] = True
            q.append((na, nb))
            if na == 0:
                ans.add(total - na - nb)

    res = sorted(ans)
    return res

def main():
    A, B, C = map(int, input().split())
    res = solve(A, B, C)
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()
