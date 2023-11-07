import sys
import collections
input = sys.stdin.readline

def movement(N: int, M: int, x: int, y: int, dir: int):
    
    ni = x + delta[dir][0]
    nj = y + delta[dir][1]
    if 0 <= ni < N and 0 <= nj < M:
        return ni ,nj, dir
    
    dir = (dir + 2) % 4
    ni = x + delta[dir][0]
    nj = y + delta[dir][1]
    return ni, nj, dir

def dir_dice(dir):
    if dir == 0: # 동쪽
        dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
    elif dir == 1: # 남쪽
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
    elif dir == 2: # 서쪽
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
    elif dir == 3: # 북쪽
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]


def get_score(N, M, x, y):
    cnt = 0
    value = arr[x][y]
    visited = {(x,y)}
    Q = [(x,y)]

    while Q:
        cnt += 1

        i, j = Q.pop()
        for d in delta:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < N and 0 <= nj < M and not (ni,nj) in visited:
                if arr[ni][nj] == value:
                    Q.append((ni,nj))
                    visited.add((ni,nj))

    return value * cnt


def new_dir(A: int, B: int, dir: int):
    if A > B:
        return (dir+1) % 4
    elif A < B:
        return 3 if dir-1 < 0 else dir - 1
    else:
        return dir


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    x, y, dir = 0, 0, 0
    dice = [2, 4, 1, 3, 5, 6]
    for k in range(K):
        x, y, dir = movement(N, M, x, y, dir) # 위치 이동
        dir_dice(dir) # 주사위 변경
        result += get_score(N, M, x, y)
        dir = new_dir(dice[5], arr[x][y],dir)

    print(result)

