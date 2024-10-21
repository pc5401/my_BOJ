import sys
import collections
input = sys.stdin.readline      


def solve(l: int, knight: tuple[int], target: tuple[int]) -> int:
    delta = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (1, -2), (2, -1)]
    visited = [[0] * l for _ in range(l)]
    x, y = target
    i, j = knight

    Q = collections.deque()
    Q.append([i, j])
    visited[i][j] = 1

    if i == x and j == y:
        return 0

    while Q:
        i, j = Q.popleft()

        for d in delta:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < l and 0 <= nj < l and not visited[ni][nj]:
                Q.append([ni, nj])
                visited[ni][nj] = visited[i][j] + 1
                if ni == x and nj == y:
                    return visited[ni][nj] -1

    return 0


if __name__ == "__main__":
    # 입력값
    T = int(input())
    L = []
    knights = []
    targets = []
    for _ in range(T):
        L.append(int(input()))
        knights.append(map(int, input().split()))
        targets.append(map(int, input().split()))

    # 풀이
    result = [solve(L[t], knights[t], targets[t]) for t in range(T)]

    # 출력
    for res in result:
        print(res)