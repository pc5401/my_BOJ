import sys
sys.setrecursionlimit(10001)
input = sys.stdin.readline


def find(node):
    if union_find[node] != node:
        union_find[node] = find(union_find[node])
    return union_find[node]


if __name__ == "__main__":
    V, E = map(int, input().split())
    grahp = [list(map(int, input().split())) for _ in range(E)]
    union_find = {i:i for i in range(1, V+1)}
    grahp.sort(key=lambda x: x[2])
    res = 0

    for a, b, c in grahp:
        A, B = find(a), find(b)
        if A == B: # 연결됨
            continue
        union_find[A] = B
        res += c

    print(res)

