import sys
from collections import deque
input = sys.stdin.readline

knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)]

def compute_moves(K: int, N: int, M: int) -> list:
    graph = [[None for _ in range(M)] for _ in range(N)]
    for r in range(N):
        for c in range(M):
            q = deque()
            q.append((r, c, 0))
            visited = [[[False]*(K+1) for _ in range(M)] for _ in range(N)]
            visited[r][c][0] = True
            level_positions = set()
            while q:
                cr, cc, d = q.popleft()
                if d > 0:
                    level_positions.add((cr, cc))
                if d < K:
                    for dr, dc in knight_moves:
                        nr, nc = cr+dr, cc+dc
                        nd = d+1
                        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc][nd]:
                            visited[nr][nc][nd] = True
                            q.append((nr, nc, nd))
            graph[r][c] = list(level_positions)
    return graph

def solve_board(N: int, M: int, board: list[str]) -> int:
    pieces = []
    for i in range(N):
        for j in range(M):
            ch = board[i][j]
            if ch != '.':
                pieces.append((i, j, int(ch)))
    move_graph = {}
    for k in range(1, 10):
        move_graph[k] = compute_moves(k, N, M)
    piece_dist = []
    for (sr, sc, k) in pieces:
        dist = [[-1]*M for _ in range(N)]
        dq = deque()
        dq.append((sr, sc))
        dist[sr][sc] = 0
        while dq:
            r, c = dq.popleft()
            for nr, nc in move_graph[k][r][c]:
                if dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    dq.append((nr, nc))
        piece_dist.append(dist)
    result = None
    for i in range(N):
        for j in range(M):
            total = 0
            possible = True
            for dist in piece_dist:
                if dist[i][j] == -1:
                    possible = False
                    break
                total += dist[i][j]
            if possible:
                if result is None or total < result:
                    result = total
    return result if result is not None else -1

def main():
    # 입력
    N, M = map(int, input().split())
    board = [input().strip() for _ in range(N)]
    
    # 풀이
    result = solve_board(N, M, board)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
