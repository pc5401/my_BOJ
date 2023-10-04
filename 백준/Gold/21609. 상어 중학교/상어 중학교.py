import sys
import collections
input = sys.stdin.readline


def block_bfs(N,i,j,Arr,visited)->tuple:
    # 블록 크기 체크 : BFS
    Q = collections.deque()
    Q.append([i, j])
    visited[i][j] = 1
    size = 0
    rainbow = 0
    color = Arr[i][j]
    zero = set()

    while Q:
        size += 1
        v = Q.popleft()
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and Arr[ni][nj] == color:
                    visited[ni][nj] = 1
                    Q.append([ni,nj])
                elif Arr[ni][nj] == 0 and not f'{ni}_{nj}' in zero:
                    Q.append([ni, nj])
                    zero.add(f'{ni}_{nj}')
                    rainbow += 1

    return size, rainbow


def target_block(N: int, Arr: int) -> tuple: 
    # 1번: 크기가 가장 큰 블록 그룹을 찾기
    visited = [[0]*N for _ in range(N)]
    r, c, rtn_size, rtn_rainbow_cnt = 0,0,0,0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and Arr[i][j] > 0:
                size, rainbow_cnt = block_bfs(N,i,j,Arr,visited)
                if size > rtn_size:
                    rtn_size = size
                    rtn_rainbow_cnt = rainbow_cnt
                    r, c = i, j
                elif size == rtn_size and rainbow_cnt > rtn_rainbow_cnt:
                    rtn_rainbow_cnt = rainbow_cnt
                    r, c = i, j
                elif size == rtn_size and rainbow_cnt == rtn_rainbow_cnt:
                    if r < i:
                        r, c = i, j
                    elif r == i and c < j:
                        r, c = i, j

    return r, c, rtn_size


def delete_block(x: int, y: int, N: int, Arr: list):
    # 블록 지워서 빈 공간 만들기
    color = Arr[x][y]
    visited = set()
    visited.add(f'{x}_{y}')
    Q = collections.deque()
    Q.append([x,y])

    while Q:
        v = Q.popleft()
        Arr[v[0]][v[1]] = -2 # 빈공간

        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]
            if 0 <= ni < N and 0 <= nj < N and not f'{ni}_{nj}' in visited:
                if Arr[ni][nj] == color or Arr[ni][nj] == 0:
                    Q.append([ni,nj])
                    visited.add(f'{ni}_{nj}')


def gravity(N: int, Arr: list):
    # 중력 작동
    for j in range(N):
        for i in range(N-2,-1,-1):
            if Arr[i][j] >= 0:
                now = i
                while now < N - 1:
                    down = now+1
                    if down < N and Arr[down][j] == -2:
                        Arr[now][j], Arr[down][j] = Arr[down][j], Arr[now][j] # 스위칭
                    else:
                        break
                    now = down
                


def turn(r, c, N, Arr):
    if r >= N // 2:
        return
    
    L = N - 1 - r*2 
    for i in range(L):
        temp = Arr[r][c+i]
        Arr[r][c+i] = Arr[r+i][c+L]
        Arr[r+i][c+L] = Arr[r+L][c+L-i]
        Arr[r+L][c+L-i] = Arr[r+L-i][c]
        Arr[r+L-i][c] = temp
    
    turn(r+1, c+1, N, Arr)


def check(N:int, Arr:list) -> bool:
    for i in range(N):
        for j in range(N):
            if Arr[i][j] >= 0:
                return True
    return False


def debug_func(N, Arr, word):
    print(f'-=-=-=-=-=- 디버깅 : {word} -=-=-=-=-=- ')
    for i in range(N):
        line = ""
        for j in range(N):
            v = Arr[i][j]
            line += f' {v} ' if v > -2 else ' ㅁ '
        print(line)

def solve(N: int, M: int, Arr: int) -> int:
    score = 0
    while check(N, Arr):
        targetX, targetY, get_score = target_block(N, Arr)
        if get_score < 2:
            break
        score += get_score**2 # 점수 추가
        delete_block(targetX, targetY, N, Arr)
        gravity(N, Arr)
        turn(0, 0, N, Arr)
        gravity(N, Arr)

    
    return score


if __name__ == "__main__":
    # 입력 & 전처리
    N, M = map(int, input().split())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    if N > 1:
        print(solve(N, M, Arr))
    else:
        print(0)

