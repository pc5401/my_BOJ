import sys
input = sys.stdin.readline

def solve(N: int, M: int, grid: list[str]) -> int:
    row_parity = [row.count('1') % 2 for row in grid]
    col_parity = []
    for j in range(M):
        cnt = sum(1 for i in range(N) if grid[i][j] == '1')
        col_parity.append(cnt % 2)
    sum_row = sum(row_parity) % 2
    sum_col = sum(col_parity) % 2

    if (sum_row + sum_col) % 2 != 0:
        return -1
    best = None

    for C in (0, 1):
        R = (sum_row + C) % 2
        r_ops = sum(1 for p in row_parity if p != C)
        c_ops = sum(1 for p in col_parity if p != R)
        total = r_ops + c_ops
        if best is None or total < best:
            best = total
    return best

def main():
    # 입력
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]
    # 풀이
    result = solve(N, M, grid)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
