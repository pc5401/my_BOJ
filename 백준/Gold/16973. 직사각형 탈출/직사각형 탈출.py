import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

H, W, Sr, Sc, Fr, Fc = map(int, input().split())
Sr -= 1
Sc -= 1
Fr -= 1
Fc -= 1

# 1. prefix sum 배열 생성
prefix = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

def can_move(r, c):
    if r < 0 or c < 0 or r+H > N or c+W > M:
        return False
    
    total = prefix[r+H][c+W] - prefix[r+H][c] - prefix[r][c+W] + prefix[r][c]
    return total == 0

# BFS 준비
dist = [[-1]*M for _ in range(N)]
dist[Sr][Sc] = 0

q = deque()
q.append((Sr, Sc))

while q:
    r, c = q.popleft()

    if r == Fr and c == Fc:
        print(dist[r][c])
        sys.exit(0)

    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M:
            # dist가 -1이면 아직 방문 안 한 상태
            if dist[nr][nc] == -1:
                # 직사각형을 nr,nc에 놓을 수 있는지 확인
                if can_move(nr, nc):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

# 이동할 수 없는 경우
print(-1)
