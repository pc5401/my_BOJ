import sys
import collections
input = sys.stdin.readline



if __name__ == "__main__":
    N, M = map(int, input().split())
    bitmap = [list(input()) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    Q = collections.deque()

    for i in range(N):
        for j in range(M):
            if bitmap[i][j] == '1':
                Q.append((i,j))
                visit[i][j] = 1

    while Q:
        r, c = Q.popleft()

        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni = r + d[0]
            nj = c + d[1]
            if 0 <= ni < N and 0 <= nj < M and not visit[ni][nj]:
                Q.append((ni, nj))
                visit[ni][nj] = visit[r][c] + 1
    
    for v in visit:
        print(*map(lambda x: x-1, v))
