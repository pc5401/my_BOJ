import sys
from collections import deque
input = sys.stdin.readline

def solve(N, M, A):
    W = 2 * M - 1
    dq = deque()
    out = []
    for j in range(N):
        while dq and A[dq[-1]] <= A[j]:
            dq.pop()
        dq.append(j)
        s = j - W + 1
        if dq[0] < s:
            dq.popleft()
        if s >= 0:
            out.append(A[dq[0]])
    return out

def main():
    # 입력
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 풀이
    result = solve(N, M, A)

    # 출력
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
