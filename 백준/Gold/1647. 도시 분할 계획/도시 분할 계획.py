import sys
input = sys.stdin.readline


def find(node):
    if union_find[node] != node:
        union_find[node] = find(union_find[node])
    return union_find[node]


if __name__ == "__main__":
    N, M = map(int, input().split())
    bills = [list(map(int, input().split())) for _ in range(M)]
    union_find = {i:i for i in range(1, N+1)}
    bills.sort(key=lambda x: x[2])
    C = 0
    res = 0

    for a, b, c in bills:
        A, B = find(a), find(b)
        if A == B: # 연결됨
            continue
        union_find[A] = B
        C = max(c, C)
        res += c

    print(res - C)