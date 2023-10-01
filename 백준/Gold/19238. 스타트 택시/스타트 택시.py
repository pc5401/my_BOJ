import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def pick_up(N: int, guest_map: list, nowX: int, nowY: int) -> tuple:
    cost = 0
    lst = []
    if guest_map[nowX][nowY] < 0: # 만약 현 위치에 손님이 있다면,
        return nowX, nowY , cost
    
    visited = [[0]*N for _ in range(N)]
    visited[nowX][nowY] = 1
    Q = deque()
    Q.append([nowX, nowY])
    
    while Q:
        i, j = Q.popleft()
        for d in [[-1,0],[0,-1],[0,1],[1,0]]:
            ni = i+d[0]
            nj = j+d[1]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if guest_map[ni][nj] == 1: # 장애물
                    visited[ni][nj] = 1
                elif guest_map[ni][nj] < 0: # 목적지
                    if cost and cost < visited[i][j]:
                        break
                    lst.append([ni,nj])
                    visited[ni][nj] = visited[i][j] + 1
                    cost = visited[i][j]
                else: # 0
                    visited[ni][nj] = visited[i][j] + 1
                    if lst: # 목적지 찾으면,
                        continue
                    Q.append([ni,nj])

    if lst:
        lst.sort(key=lambda x: (x[0], x[1]))
        return lst[0][0], lst[0][1], cost
    return 0, 0, 1e9


def drop_off(N: int, guest_map: list, guest_info: dict, nowX: int, nowY: int):
    
    visited = [[0]*N for _ in range(N)]
    visited[nowX][nowY] = 1
    Q = deque()
    Q.append([nowX, nowY])
    x, y = guest_info[f'{nowX}_{nowY}']

    while Q:
        i, j = Q.popleft()
        if i == x and j == y: #도착
            return x, y, visited[i][j] - 1
        for d in [[-1,0],[0,-1],[0,1],[1,0]]:
            ni = i+d[0]
            nj = j+d[1]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if guest_map[ni][nj] == 1: # 장애물
                    visited[ni][nj] = 1
                else: # 0
                    visited[ni][nj] = visited[i][j] + 1
                    Q.append([ni,nj])

    return x, y, -1


def solve(N: int, M: int, Fuel: int, guest_map: list, Start: list, guest_info: dict) -> list:
    fuel = Fuel
    nowX, nowY = Start
    for _ in range(M):
        # 손님 태우려 가기
        nowX, nowY, cost = pick_up(N, guest_map, nowX, nowY)
        if cost > fuel:
            return -1
        guest_map[nowX][nowY] = 0
        fuel -= cost
        # 목적지까지 데려다 주기
        nowX, nowY, profit = drop_off(N, guest_map, guest_info, nowX, nowY)
        if profit > fuel or profit < 0:
            return -1

        fuel += profit
    # 손님 다 태움
    return fuel

if __name__ == "__main__":
    # 입력 & 전처리
    N, M, Fuel = map(int, input().split())
    guest_map = [list(map(int, input().split())) for _ in range(N)]
    Start = list(map(lambda x: int(x)-1 ,input().split()))
    guest_info = defaultdict(list)
    for _ in range(M):
        x,y,r,c = map(lambda x: int(x)-1, input().split())
        guest_info[f'{x}_{y}'] = [r, c]
        guest_map[x][y] = -2
    # 연산 함수 실행 및 출력
    print(solve(N, M, Fuel, guest_map, Start, guest_info))

