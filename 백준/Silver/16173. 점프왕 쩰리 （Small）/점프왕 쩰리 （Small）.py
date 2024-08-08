import sys
input = sys.stdin.readline


def solve(N: int, arr: list[list[int]]):
    Q = [(0, 0)]

    while Q:
        i, j = Q.pop()
        v = arr[i][j]
        if v == -1:
            return 'HaruHaru'
        elif v == 0:
            continue

        for d in ((1, 0),(0, 1)):
            ni = i + d[0]*v
            nj = j + d[1]*v
            if 0 <= ni < N and 0 <= nj < N:
                Q.append((ni, nj))

    return 'Hing'


def main():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, arr))

main()