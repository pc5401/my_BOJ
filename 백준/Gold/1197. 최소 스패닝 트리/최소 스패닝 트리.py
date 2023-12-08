import sys
input = sys.stdin.readline


def find(node):
    if union_find[node] != node:
        union_find[node] = find(union_find[node])
    
    return union_find[node] # 재귀


def union(a, b):
    A, B = find(a), find(b)
    if A != B:
        union_find[A] = B


if __name__ == "__main__":
    V, E = map(int, input().split())
    lst = [list(map(int,input().split())) for _ in range(E)]
    lst.sort(key=lambda x: x[2])
    res = 0
    union_find = { i:i for i in range(1, V+1)}

    for a, b, c in lst:
        if find(a) != find(b):
            union(a, b)
            res += c
    print(res)