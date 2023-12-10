import sys
input = sys.stdin.readline


def find(node: int):
    if union_find[node] != node:
        union_find[node] = find(union_find[node])
    
    return union_find[node]


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    networds = [tuple(map(int, input().split())) for _ in range(M)]
    networds.sort(key=lambda x : x[2])
    union_find = {i:i for i in range(1,N+1)}
    result = 0

    for a, b, c in networds:
        A, B = find(a), find(b)
        if A != B:
            union_find[A] = B
            result += c

    print(result)