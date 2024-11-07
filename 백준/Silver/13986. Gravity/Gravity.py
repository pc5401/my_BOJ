import sys
input = sys.stdin.readline


def drop_apple(i, j, n, grid):

    for x in range(i, n-1):
        if grid[x+1][j] == '.':
            grid[x][j], grid[x+1][j] = grid[x+1][j], grid[x][j]
        else:
            return



def solve(N: int, M: int, grid: list[list[str]]) -> int:

    for j in range(M):
        for i in range(N-1, -1, -1):
            if grid[i][j] == 'o':
                drop_apple(i, j, N, grid)


    rtn = ["".join(g) for g in grid]
    return rtn


def main():
    # 입력값
    N, M = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(N)]
    
    # 풀이
    result = solve(N, M, grid)
    
    # 출력
    for res in result:
        print(res)

if __name__ == '__main__':
    main()
