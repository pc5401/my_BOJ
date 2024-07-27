import sys
import collections
input = sys.stdin.readline


def solve(K: int, W: int, H: int, arr: list[list[int]]):
    rtn = float('inf')
    Q = collections.deque()
    Q.append([0, 0, K, 0])
    visited = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]
    visited[0][0][K] = 1

    delta = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    horse = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]

    while Q:
        i, j, k, s = Q.popleft()

        if s >= rtn:
            continue

        if i == H-1 and j == W-1:
            rtn = min(rtn, s)
            continue

        for n, m in delta:
            ni = i + n
            nj = j + m
            if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] != 1 and not visited[ni][nj][k]:
                Q.append([ni, nj, k, s+1])
                visited[ni][nj][k] = 1

        if (k > 0):
            for n, m in horse:
                ni = i + n
                nj = j + m
                if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] != 1 and not visited[ni][nj][k-1]:
                    Q.append([ni, nj, k-1, s+1])
                    visited[ni][nj][k-1] = 1
        

    
    return rtn if rtn != float('INF') else -1


def main():
    K = int(input())
    W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    print(solve(K, W, H, arr))
main()


