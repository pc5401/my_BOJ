import sys
from collections import deque
input = sys.stdin.readline


def rotate_circles(N: int, circles: list, rotation: list):
    x, d, k = rotation
    for i in range(x-1, N, x):
        for _ in range(k):
            if d: # 1이면 반시계 방향
                v = circles[i].popleft()
                circles[i].append(v)
            else: # 시계방향
                v = circles[i].pop()
                circles[i].appendleft(v)


def bfs(N, M, i, j, visited, circles):

    Q = deque()
    Q.append([i, j])
    value = circles[i][j]
    visited[i][j] = 1

    while Q:
        r, c = Q.popleft()
        
        for d in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr = r+d[0]
                nc = c+d[1]
                
                if nc >= M:
                    nc = 0
                elif nc < 0:
                    nc = M-1

                if 0 <= nr < N:
                    if circles[nr][nc] == value and not visited[nr][nc]:
                        Q.append([nr, nc])
                        visited[nr][nc] = 1


def change_number(N, M, circles):
    sumV, cnt = 0, 0
    flag = 0
    visited = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue

            for d in [(0,1),(1,0),(-1,0),(0,-1)]:
                ni = i+d[0]
                nj = j+d[1]

                if nj >= M:
                    nj = 0
                elif nj < 0:
                    nj = M-1
                
                if 0 <= ni < N and circles[i][j]:
                    if circles[i][j] == circles[ni][nj]:
                        bfs(N, M, i, j, visited, circles)
                        flag = 1
                        break
            
            if visited[i][j] == 0 and circles[i][j] > 0:
                visited[i][j] = 2
                cnt += 1
                sumV += circles[i][j]
            
            elif visited[i][j] == 0:
                visited[i][j] = 3

    if flag == 1: # 인접 수 존재
        for i in range(N):
            for j in range(M):
                if visited[i][j] == 1:
                    circles[i][j] = 0
    else: # 인접 수 X
        if cnt:
            avg = sumV / cnt
        else:
            avg = 0
        for i in range(N):
            for j in range(M):
                if visited[i][j] == 2:
                    if circles[i][j] > avg:
                        circles[i][j] -= 1
                    elif circles[i][j] < avg:
                        circles[i][j] += 1



def solve(N: int, M: int, T: int, circles: int, rotation_lst: int):
    
    for rotation in rotation_lst:
        rotate_circles(N, circles, rotation)
        change_number(N, M, circles)

    res = 0
    for circle in circles:
        res += sum(circle)

    return res


if __name__ == "__main__":
    # 입력 & 전처리
    N, M, T = map(int,input().split())
    circles = [deque(map(int, input().split())) for _ in range(N)]
    rotation_lst = [list(map(int, input().split())) for _ in range(T)]
    print(solve(N, M, T, circles, rotation_lst))
