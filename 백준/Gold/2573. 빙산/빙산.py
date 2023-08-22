import sys
input = sys.stdin.readline

def melt_ice(sea):
    global N, M
    melting_points = []
    for i in range(N):
        for j in range(M):
            if sea[i][j]: # 얼음이여
                cnt = 0
                for d in [[0,1],[0,-1],[1,0],[-1,0]]:
                    ni = i + d[0]
                    nj = j + d[1]
                    if 0 <= ni < N and 0 <= nj < M and sea[ni][nj] == 0:
                        cnt += 1
                melting_points.append((i, j, cnt))

    for i, j, cnt in melting_points: # 빙하 녹이기
        sea[i][j] = max(sea[i][j] - cnt, 0)  # max 함수로 0보다 작으면 0


def count_ice(sea):
    global N, M
    visit = [[0]*M for _ in range(N)] # 방문
    delta = [[0,1],[0,-1],[1,0],[-1,0]]
    
    def dfs(x, y):
        visit[x][y] = 1
        Q = [[x,y]]
        while Q:
            v = Q.pop()

            for d in delta:
                nx = v[0] + d[0] 
                ny = v[1] + d[1]
                if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and sea[nx][ny]:
                    Q.append([nx, ny])
                    visit[nx][ny] = 1
    
    parts = 0
    for i in range(N):
        for j in range(M):
            if sea[i][j] and not visit[i][j]:
                dfs(i, j)
                parts += 1
    return parts


def get_time(n, m, sea):
    global N, M
    N, M = n, m
    time = 0

    while True:
        melt_ice(sea) # 빙하 먼저 녹이기
        time += 1 # 시간 올림
        parts = count_ice(sea) # 몇 개의 빙하가 있는지
        if parts >= 2:
            return time
        elif parts == 0:
            return 0
        # 1 개면 다시 순회

if __name__ == '__main__':
    N, M = map(int,input().split())
    sea = [ list(map(int, input().split())) for _ in range(N) ]
    print(get_time(N, M, sea))

