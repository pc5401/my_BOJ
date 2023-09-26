import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def movement(N: int, number: int, ocean: list, location_shark: list, direction_shark: list, direction_list: list, delta: list):
    i, j = location_shark[number][-1] # 마지막 위치
    dir = direction_shark[number] # 바라보는 방향
    dir_list = direction_list[number][dir]

    # 냄새 없는 곳
    for d in dir_list:
        ni, nj = i + delta[d][0], j + delta[d][1]
        if 0 <= ni < N and 0 <= nj < N and ocean[ni][nj] == 0:
            location_shark[number].append([ni, nj])
            direction_shark[number] = d
            return (ni, nj)
        
    # 냄새 있는 곳
    for d in dir_list:
        ni, nj = i + delta[d][0], j + delta[d][1]
        if 0 <= ni < N and 0 <= nj < N and ocean[ni][nj]  == number:
            location_shark[number].append([ni, nj])
            direction_shark[number] = d
            return (ni, nj)
    
    location_shark.append([i, j])
    return (i, j)


def check_movement(shark_moved: list, ocean: list, life: list):
    visited = set()
    for x, y, number in shark_moved:
        if f'{x}_{y}' in visited:
            life[number] = 0
            continue
        visited.add(f'{x}_{y}')
        ocean[x][y] = number


def del_smell(M: int, location_shark: list, ocean: list):
    for number in range(1, M+1):
        if not location_shark[number]:
            continue
        
        i, j = location_shark[number].popleft()
        if ocean[i][j] == number:
            ocean[i][j] = 0
        if [i,j] in location_shark[number]:
            ocean[i][j] = number



def solve(N: int, M: int, K: int, ocean: list, location_shark: list, direction_shark: list, direction_list: list, delta: list) -> int:
    life = [1] * (M+1)
    life[0] = 0
    
    for time in range(1, 1001):
        shark_moved = []
        for number in range(1, M+1):
            if life[number] == 0:
                continue
            nx, ny = movement(N,number, ocean, location_shark, direction_shark, direction_list, delta)
            shark_moved.append([nx, ny, number])

        check_movement(shark_moved, ocean, life)
        
        if time >= K:
            del_smell(M, location_shark, ocean)

        if sum(life) == 1:
            return time

    return -1


if __name__ == "__main__":
    # 입력 & 전처리
    N, M, K = map(int,input().split())
    location_shark = defaultdict(deque)
    ocean = []
    for i in range(N):
        lst = list(map(int, input().split()))
        for j in range(N):
            if lst[j] > 0:
                location_shark[lst[j]].append([i,j])
        ocean.append(lst)
    direction_shark = [0] + list(map(int, input().split()))
    direction_list = defaultdict(list)
    for shark_number in range(1,M+1):
        direction_list[shark_number].append([0,0,0,0])
        for _ in range(4):
            direction_list[shark_number].append(list(map(int, input().split())))
    delta = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]

    print(solve(N, M, K, ocean, location_shark, direction_shark, direction_list, delta))
