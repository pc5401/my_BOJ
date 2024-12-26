import sys
from collections import deque
input = sys.stdin.readline


def can_clear(N, A, j):
    visited = [0] * (N+3)
    visited[1] = 1
    queue = deque([1])

    while queue:
        pos = queue.popleft()
        if pos >= N+2:
            return 1
        for dice_num in range(1, j+1):
            nxt = pos + dice_num
            if nxt >= N+2:
                return 1
            if A[nxt - 2] == 1:
                continue
            if not visited[nxt]:
                visited[nxt] = 1
                queue.append(nxt)
    return 0


def solve(N: int, A: list[int]) -> int:
    for i in range(1, N+2):
        if can_clear(N, A, i):
            return i



if __name__ == '__main__':
    # 입력값
    N = int(input())
    A = list(map(int, input().split()))

    # 풀이
    result = solve(N, A)

    # 출력
    print(result)