import sys
input = sys.stdin.readline

def solve(n: int, W: int, H: int, trees: list[tuple[int, int]], S: int, T: int) -> int:
    grid = [[0] * (H + 1) for _ in range(W + 1)]
    for x, y in trees:
        grid[x][y] = 1

    ps = [[0] * (H + 1) for _ in range(W + 1)]
    for i in range(1, W + 1):
        for j in range(1, H + 1):
            ps[i][j] = grid[i][j] + ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1]
    
    max_trees = 0
    for i in range(1, W - S + 2):
        for j in range(1, H - T + 2):
            x1, y1 = i, j
            x2, y2 = i + S - 1, j + T - 1
            count = ps[x2][y2] - ps[x1 - 1][y2] - ps[x2][y1 - 1] + ps[x1 - 1][y1 - 1]
            if count > max_trees:
                max_trees = count
    return max_trees

def main():
    # 입력
    while True:
        line = input().strip()
        if line == "0":
            break
        N = int(line)
        W, H = map(int, input().split())
        trees = []
        for _ in range(N):
            x, y = map(int, input().split())
            trees.append((x, y))
        S, T = map(int, input().split())
        
        # 풀이
        result = solve(N, W, H, trees, S, T)
        
        # 출력
        print(result)

if __name__ == "__main__":
    main()
