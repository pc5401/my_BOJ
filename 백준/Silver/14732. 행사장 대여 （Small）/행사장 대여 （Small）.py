import sys
input = sys.stdin.readline

def solve(rects: list[tuple[int,int,int,int]]) -> int:
    max_coord = 500
    grid = [[False]*(max_coord+1) for _ in range(max_coord+1)]
    for x1, y1, x2, y2 in rects:
        for x in range(x1, x2):
            row = grid[x]
            for y in range(y1, y2):
                row[y] = True
    area = 0
    for x in range(max_coord+1):
        area += sum(grid[x])
    return area

def main():
    # 입력
    N = int(input().strip())
    rects = [tuple(map(int, input().split())) for _ in range(N)]
    # 풀이
    result = solve(rects)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
