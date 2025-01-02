import sys
input = sys.stdin.readline

def solve(N: int, cmd: str) -> list[str]:
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    direction = 2
    x, y = 0, 0
    visited = set()
    visited.add((x, y))
    for c in cmd:
        if c == 'F':
            dx, dy = dirs[direction]
            x += dx
            y += dy
            visited.add((x, y))
        elif c == 'L':
            direction = (direction - 1) % 4
        elif c == 'R':
            direction = (direction + 1) % 4
    min_x = min(px for px, py in visited)
    max_x = max(px for px, py in visited)
    min_y = min(py for px, py in visited)
    max_y = max(py for px, py in visited)
    height = max_x - min_x + 1
    width = max_y - min_y + 1
    grid = [['#'] * width for _ in range(height)]
    for xx, yy in visited:
        grid[xx - min_x][yy - min_y] = '.'
    result = []
    for row_idx in range(height):
        result.append(''.join(grid[row_idx]))
    return result

if __name__ == "__main__":
    N = int(input())
    cmd = input().rstrip()
    result = solve(N, cmd)
    for res in result:
        print(res)
