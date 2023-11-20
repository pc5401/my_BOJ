import sys
import itertools
input = sys.stdin.readline

def look_for(target: str, n: int):
    rtn = []
    for i in range(n):
        for j in range(n):
            if room[i][j] == target:
                rtn.append((i,j))
    return rtn

def eyesight(n: int):
    rtn = set()
    
    for teacher in teachers:
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            flag = 0
            lst = []
            ni = teacher[0] + d[0]
            nj = teacher[1] + d[1]
            while 0 <= ni < n and 0 <= nj < n:
                if room[ni][nj] == 'T':
                    break
                elif room[ni][nj] == 'S':
                    flag = 1
                else:
                    lst.append((ni, nj))
                ni += d[0]
                nj += d[1]
            
            if flag and lst:
                for v in lst:
                    rtn.add(v)
    return rtn


def teachers_bfs(n):
    
    for teacher in teachers:
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni = teacher[0] + d[0]
            nj = teacher[1] + d[1]
            while 0 <= ni < n and 0 <= nj < n:
                if room[ni][nj] == 'S':
                    return 0
                elif room[ni][nj] == 'O' or room[ni][nj] == 'T' :
                    break
                ni += d[0]
                nj += d[1]
    return 1


def OX(val: str, arr: list):
    for x, y in arr:
        room[x][y] = val

if __name__ == "__main__":
    N = int(input())
    room = [list(input().split()) for _ in range(N)]
    teachers = look_for('T', N)
    eyes = eyesight(N)
    eyes_len = len(eyes)

    res = 'NO'
    if eyes_len == 0:
        res = 'YES'
    elif eyes_len == 1:
        for x,y in eyes:
            room[x][y] = 'O'
            if teachers_bfs(N):
                res = 'YES'
                break
            room[x][y] = 'X'
            
    elif eyes_len == 2:
        X_lst = itertools.combinations(eyes, 2)
        for X_val in X_lst:
            OX('O', X_val)
            if teachers_bfs(N):
                res = 'YES'
                break
            OX('X', X_val)

    else:
        X_lst = itertools.combinations(eyes, 3)
        for X_val in X_lst:
            OX('O', X_val)
            if teachers_bfs(N):
                res = 'YES'
                break
            OX('X', X_val)

    print(res)