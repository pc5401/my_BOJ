import sys
input = sys.stdin.readline

def solve(n: int, r: int, F: list[list[int]]) -> list[list[int]]:
    P = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        row_sum = 0
        for j in range(1, n+1):
            row_sum += F[i-1][j-1]
            P[i][j] = P[i-1][j] + row_sum

    W = [[0]*n for _ in range(n)]
    for i in range(1, n+1):
        x1 = max(1, i - r)
        x2 = min(n, i + r)
        for j in range(1, n+1):
            y1 = max(1, j - r)
            y2 = min(n, j + r)
            W[i-1][j-1] = (
                P[x2][y2]
                - P[x1-1][y2]
                - P[x2][y1-1]
                + P[x1-1][y1-1]
            )
    return W

def main():
    # 입력
    n, r = map(int, input().split())
    F = [list(map(int, input().split())) for _ in range(n)]
    # 풀이
    W = solve(n, r, F)
    # 출력
    for row in W:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
