import sys
from collections import deque
input = sys.stdin.readline

def solve(R: int, C: int, grid: list[str]) -> int:
    visited = [[False]*C for _ in range(R)]
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    count = 0

    for i in range(R):
        for j in range(C):
            if grid[i][j] == '#' and not visited[i][j]:
                count += 1
                # BFS로 하나의 뭉치 탐색
                dq = deque()
                dq.append((i,j))
                visited[i][j] = True
                while dq:
                    r, c = dq.popleft()
                    for d in range(4):
                        nr, nc = r+dr[d], c+dc[d]
                        if 0 <= nr < R and 0 <= nc < C:
                            if grid[nr][nc] == '#' and not visited[nr][nc]:
                                visited[nr][nc] = True
                                dq.append((nr,nc))
    return count

def main():
    # 입력
    R, C = map(int, input().split())
    grid = [input().rstrip() for _ in range(R)]
    # 풀이
    result = solve(R, C, grid)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
