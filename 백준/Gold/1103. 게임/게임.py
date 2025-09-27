import sys
input = sys.stdin.readline

def solve(N, M, board):
    sys.setrecursionlimit(10000000)
    dp = [[-1] * M for _ in range(N)]
    inpath = [[False] * M for _ in range(N)]
    infinity = [False]

    def dfs(r, c):
        if r < 0 or r >= N or c < 0 or c >= M or board[r][c] == 'H':
            return 0
        if inpath[r][c]:
            infinity[0] = True
            return 0
        if dp[r][c] != -1:
            return dp[r][c]

        inpath[r][c] = True
        v = ord(board[r][c]) - 48
        best = 0
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr * v, c + dc * v
            val = dfs(nr, nc)
            if infinity[0]:
                return 0
            if val > best:
                best = val
        inpath[r][c] = False
        dp[r][c] = best + 1
        return dp[r][c]

    res = dfs(0, 0)
    return -1 if infinity[0] else res

def main():
    # 입력
    N, M = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]

    # 풀이
    result = solve(N, M, board)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
