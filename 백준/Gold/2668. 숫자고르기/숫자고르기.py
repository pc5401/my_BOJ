import sys
input = sys.stdin.readline


def graph_move(idx: int, n: int):
    A, B = [], []
    visited = [0]*n
    i = idx
    while visited[i] == 0:
        visited[i] = 1
        A.append(i)
        b = lst[i]-1
        B.append(b)
        i = b

    if len(A) != len(B):
        return
    
    for a in A:
        if not a in B:
            return
    
    for a in A:
        res[a] = 1


if __name__ == "__main__":
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    res = [0] * N
    for idx in range(N):
        if res[idx]:
            continue
        graph_move(idx, N)

    print(sum(res))
    for i, r in enumerate(res):
        if r:
            print(i+1)
