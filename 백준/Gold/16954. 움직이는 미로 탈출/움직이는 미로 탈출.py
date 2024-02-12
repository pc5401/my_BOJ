import sys
import collections
input = sys.stdin.readline

def look_for_blocks():
    rtn = []
    for i in range(8):
        for j in range(8):
            if arr[i][j] == '#':
                rtn.append((i,j))
    return rtn


def movement(Q: collections.deque) -> collections.deque:
    rtn = collections.deque()
    
    while Q:
        x, y = Q.popleft()

        if arr[x][y] == '#':
            continue

        for d in [(0,0),(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1)]:
            ni = x + d[0]
            nj = y + d[1]
            if 0 <= ni < 8 and 0 <= nj < 8:
                if arr[ni][nj] == '.' and arr[x][y] == 'a':
                    arr[ni][nj] = 'a'
                    rtn.append((ni, nj))
                elif d == (0,0):
                    rtn.append((ni, nj))
    
    return rtn


def moveing_blocks(arr: list, blocks: list):
    rtn = []
    blocks.sort(key=lambda x: -x[0])
    for x, y in blocks:
        if x + 1 < 8:
            arr[x][y] = '.'
            arr[x+1][y] = '#'
            rtn.append((x+1,y))
        elif x == 7:
            arr[x][y] = '.'
    return rtn



if __name__ == '__main__':
    arr = [list(input().rstrip()) for _ in range(8)]
    blocks = look_for_blocks()
    Q = collections.deque()
    Q.append((7,0))
    arr[7][0] = 'a'

    result = 0

    while True:

        Q = movement(Q)
        if arr[0][7] == 'a':
            result = 1
            break
        
        if not Q:
            break

        blocks = moveing_blocks(arr, blocks)

    print(result)
