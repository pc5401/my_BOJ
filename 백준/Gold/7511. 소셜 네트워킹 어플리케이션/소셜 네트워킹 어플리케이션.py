import sys
input = sys.stdin.readline


def find(v):
    if union_find[v] != v:
        union_find[v] = find(union_find[v])
    return union_find[v]


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        n = int(input())
        k = int(input())
        ab = [tuple(map(int, input().split())) for _ in range(k)]
        m = int(input())
        uv = [tuple(map(int, input().split())) for _ in range(m)]
        union_find = {i:i for i in range(n)}
        for a, b in ab:
            A, B = find(a), find(b)
            if A != B:
                union_find[A] = B
        res = []
        for u, v in uv:
            if find(u) != find(v):
                res.append(0)
            else:
                res.append(1)
        
        print(f'Scenario {tc}:')
        for r in res:
            print(r)
        print()
