import sys
import heapq
input = sys.stdin.readline

def solve(n: int, m: int, grid: list[list[int]]) -> int:
    visited = [[False]*m for _ in range(n)]
    pq = []
    
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                heapq.heappush(pq, (grid[i][j], i, j))
                visited[i][j] = True
    
    trapped_water = 0
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    
    while pq:
        h, x, y = heapq.heappop(pq)
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                nh = grid[nx][ny]

                if nh < h:
                    trapped_water += h - nh
                    nh = h
                heapq.heappush(pq, (nh, nx, ny))
    
    return trapped_water

def main():
    # 입력
    n, m = map(int, input().split())
    grid = [list(map(int, list(input().strip()))) for _ in range(n)]

    # 풀이
    result = solve(n, m, grid)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
