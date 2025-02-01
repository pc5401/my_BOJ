# chatGPT o3-mini-high test

import sys
from collections import deque
input = sys.stdin.readline

def solve():
    R, C = map(int, input().split())
    lake = [list(input().rstrip()) for _ in range(R)]
    
    waterQ = deque()    # 얼음이 녹을 물의 경계 (녹은 물의 좌표)
    swanQ = deque()     # 현재 날에 백조가 이동 가능한 물 영역
    swan_next = deque() # 다음 날에 탐색할 후보 (현재 얼음이지만, 녹으면 이동 가능)
    visited = [[False] * C for _ in range(R)]
    swans = []
    
    # 초기화: 
    #  - 모든 물 또는 백조가 있는 칸은 물로 취급하여 waterQ에 넣음.
    #  - 백조의 좌표를 따로 기록.
    for i in range(R):
        for j in range(C):
            if lake[i][j] != 'X':
                waterQ.append((i, j))
            if lake[i][j] == 'L':
                swans.append((i, j))
    
    start = swans[0]
    end = swans[1]
    swanQ.append(start)
    visited[start[0]][start[1]] = True

    # 상하좌우 이동
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    day = 0

    # 시뮬레이션: 백조가 만날 수 있을 때까지 매일 진행
    while True:
        # [1] 백조 이동 BFS: 현재 물을 통해 이동 가능한 영역을 탐색.
        found = False
        while swanQ:
            x, y = swanQ.popleft()
            if (x, y) == end:
                found = True
                break
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # 현재 물(또는 백조 위치)이면 바로 이동.
                    if lake[nx][ny] == '.' or lake[nx][ny] == 'L':
                        swanQ.append((nx, ny))
                    # 얼음이면, 녹은 후 다음날 이동할 후보로 등록.
                    elif lake[nx][ny] == 'X':
                        swan_next.append((nx, ny))
        if found:
            sys.stdout.write(str(day))
            return

        # [2] 얼음 녹이기 BFS: 현재 물과 인접한 얼음을 녹여 물로 변경.
        new_water = deque()
        while waterQ:
            x, y = waterQ.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    if lake[nx][ny] == 'X':
                        lake[nx][ny] = '.'
                        new_water.append((nx, ny))
        waterQ = new_water

        # 백조 이동 후보 업데이트 (다음 날)
        swanQ = swan_next
        swan_next = deque()
        day += 1

if __name__ == '__main__':
    solve()
