import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a, b = 0, 0
    res = []

    while a < N and b < M:
        if A[a] < B[b]:
            res.append(A[a])
            a += 1
        elif A[a] > B[b]:
            res.append(B[b])
            b += 1
        else:
            res.append(A[a])
            res.append(B[b])
            a += 1
            b += 1
    
    if a < N:
        for i in range(a, N):
            res.append(A[i])
    
    if b < M:
        for i in range(b, M):
            res.append(B[i])
    
    print(*res)



