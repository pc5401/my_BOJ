import sys

def solve(R, C, grid):
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    res = []
    for i in range(R):
        row = []
        for j in range(C):
            if grid[i][j] == '*':
                row.append('*')
            else:
                cnt = 0
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < R and 0 <= y < C and grid[x][y] == '*':
                        cnt += 1
                row.append(str(cnt))
        res.append(''.join(row))
    return res

def main():
    #입력
    input = sys.stdin.readline
    outs = []
    while True:
        line = input().strip()
        if not line:
            continue
        R, C = map(int, line.split())
        if R == 0 and C == 0:
            break
        grid = [list(input().strip()) for _ in range(R)]
        #풀이
        ans = solve(R, C, grid)
        #출력
        outs.extend(ans)
    print('\n'.join(outs))

if __name__ == "__main__":
    main()
