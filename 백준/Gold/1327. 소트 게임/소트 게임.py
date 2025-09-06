import sys
from collections import deque
input = sys.stdin.readline

def solve(N, K, A):
    start = tuple(A)
    target = tuple(range(1, N + 1))
    if start == target:
        return 0

    q = deque([start])
    dist = {start: 0}

    while q:
        cur = q.popleft()
        d = dist[cur]
        for i in range(N - K + 1):
            nxt = cur[:i] + tuple(reversed(cur[i:i+K])) + cur[i+K:]
            if nxt in dist:
                continue
            if nxt == target:
                return d + 1
            dist[nxt] = d + 1
            q.append(nxt)
    return -1

def main():
    # 입력
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 풀이
    result = solve(N, K, A)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
