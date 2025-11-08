import sys

def solve(n, m, grid):
    S = [[0] * (m + 2) for _ in range(n + 2)]
    ans = 0
    for i in range(n, 0, -1):
        row = grid[i - 1]
        for j in range(m, 0, -1):
            parity = (S[i + 1][j] + S[i][j + 1] - S[i + 1][j + 1]) & 1
            cur = row[j - 1] ^ parity
            if cur == 1:
                ans += 1
                S[i][j] = parity ^ 1
            else:
                S[i][j] = parity
    return ans

def main():
    #입력
    input = sys.stdin.readline
    n, m = map(int, input().split())
    grid = [list(map(int, list(input().strip()))) for _ in range(n)]
    #풀이
    ans = solve(n, m, grid)
    #출력
    print(ans)

if __name__ == "__main__":
    main()
