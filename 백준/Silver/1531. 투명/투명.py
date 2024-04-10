import sys
input = sys.stdin.readline


def solve(N, M, papers) -> int:
    paint = [[0] * 100 for _ in range(100)]

    for lx, ly, rx, ry in papers:
        for i in range(lx-1, rx, 1):
            for j in range(ly-1, ry, 1):
                paint[i][j] += 1
    
    cnt = 0

    for i in range(100):
        for j in range(100):
            if paint[i][j] > M:
                cnt += 1

    return cnt


def main():
    N, M = map(int, input().split())
    papers = [tuple(map(int, input().split())) for _ in range(N)]
    print(solve(N, M, papers))


if __name__ == "__main__":
    main()
