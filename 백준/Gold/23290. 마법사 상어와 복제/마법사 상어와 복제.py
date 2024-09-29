import sys
import copy
input = sys.stdin.readline

def moving_fish(fish_data: list[list[list[int]]], limited: list[list[int]]) -> list[list[list[int]]]:
    delta = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
    fish_moved = [[[0] * 8 for _ in range(4)] for _ in range(4)]

    for x in range(4):
        for y in range(4):
            for d in range(8):
                if not fish_data[x][y][d]:
                    continue
                flag = False
                for i in range(8):
                    nd = (d - i) % 8
                    nx = x + delta[nd][0]
                    ny = y + delta[nd][1]
                    if 0 <= nx < 4 and 0 <= ny < 4 and not limited[nx][ny]:
                        fish_moved[nx][ny][nd] += fish_data[x][y][d]
                        flag = True
                        break
                if not flag:
                    fish_moved[x][y][d] += fish_data[x][y][d]
                    
    return fish_moved


def kill_fish_cnt(shark: list[int], path: list[int], delta: list[int], fish_data: list[list[list[int]]]) -> int:
    rtn = 0
    x, y = shark
    visited = set()
    for d in path:
        ni = x + delta[d][0]
        nj = y + delta[d][1]
        if 0 <= ni < 4 and 0 <= nj < 4:
            if not (ni, nj) in visited:
                rtn += sum(fish_data[ni][nj])
            visited.add((ni, nj))
            x = ni
            y = nj
        else:
            return -1
    
    return rtn


def moving_shark(shark: list[int], fish_data: list[list[list[int]]], limited:list[list[int]]):
    delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
    max_cnt = -1
    move_path = [0, 0, 0]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                path = [a, b, c]
                cnt = kill_fish_cnt(shark, path, delta, fish_data)
                if cnt == -1:
                    continue

                if max_cnt < cnt:
                    max_cnt = cnt
                    move_path = path

    
    for d in move_path:
        ni = shark[0] + delta[d][0]
        nj = shark[1] + delta[d][1]
        if 0 <= ni < 4 and 0 <= nj < 4:
            if any(fish_data[ni][nj]):
                for i in range(8):
                    fish_data[ni][nj][i] = 0
                limited[ni][nj] = 3
            shark[0] = ni
            shark[1] = nj
            
    
    # limited 설정 및 상어 위치
    for i in range(4):
        for j in range(4):
            if limited[i][j] > 0:
                limited[i][j] -= 1
    
    if limited[shark[0]][shark[1]] == 0:
        limited[shark[0]][shark[1]] = 1


def add_copy_fish(fish_data: list[list[list[int]]], copy_fish_data: list[list[list[int]]]):
    for i in range(4):
        for j in range(4):
            for d in range(8):
                fish_data[i][j][d] += copy_fish_data[i][j][d]


def solve(S: int, fish_data: list[list[list[int]]], shark: list[int]) -> int:
    limited = [[0] * 4 for _ in range(4)]
    limited[shark[0]][shark[1]] = 1
    
    for s in range(S):
        copy_fish_data = copy.deepcopy(fish_data) # 복사
        fish_data = moving_fish(fish_data, limited)
        moving_shark(shark, fish_data, limited)
        add_copy_fish(fish_data, copy_fish_data)

    return sum([sum([sum([c for c in b]) for b in a]) for a in fish_data])


if __name__ == "__main__":
    # 입력값
    M, S = map(int, input().split())
    fish_data = [[[0] * 8 for _ in range(4)] for _ in range(4)]
    for _ in range(M):
        x, y, d = map(int, input().split())
        fish_data[x-1][y-1][d-1] += 1
    shark = list(map(int, input().split()))
    shark[0] -= 1
    shark[1] -= 1

    # 풀이
    result = solve(S, fish_data, shark)

    # 출력
    print(result)
