import sys
input = sys.stdin.readline


def direction(dir: str):
    if dir == 'D': # 오른쪽
        board[head[0]][head[1]] = (board[head[0]][head[1]] + 1) % 4
    else:
        board[head[0]][head[1]] = (board[head[0]][head[1]] - 1) if board[head[0]][head[1]] - 1 >= 0 else 3


def movement() -> tuple:
    global N
    d = board[head[0]][head[1]]
    
    ni = head[0] + delta[d][0]
    nj = head[1] + delta[d][1]
    if 0 <= ni < N and 0 <= nj < N: # 보드 안
        if board[ni][nj] == 4: # 사과
            head[0] = ni
            head[1] = nj
            board[ni][nj] = d
            return False
        
        elif board[ni][nj] == -1: # 빈 공간
            head[0] = ni
            head[1] = nj
            board[ni][nj] = d
            t_d = board[tail[0]][tail[1]]
            ti = tail[0] + delta[t_d][0]
            tj = tail[1] + delta[t_d][1]
            board[tail[0]][tail[1]] = -1
            tail[0], tail[1] = ti, tj
            return False

        else: # 0~3 뱀 몸
            return True
    
    else: # 벽 충돌
        return True


if __name__ == '__main__':
    # 초기값 
    delta = [[0,1],[1,0],[0,-1],[-1,0]]
    head, tail = [0,0], [0,0]
    is_stop = False
    
    # 입력값
    N = int(input()) # 보드 크기
    board = [[-1] * N for _ in range(N)]
    K = int(input()) # 사과
    for _ in range(K):
        x, y = map(int, input().split())
        board[x-1][y-1] = 4
    board[0][0] = 0
    L = int(input()) # 움직임
    move_lst = [list(input().rstrip().split()) for l in range(L)]
    
    time = 0
    x, D = move_lst.pop(0)
    X = int(x)
    while True:
        time += 1
        if movement():
            break

        if time == X:
            direction(D)
            if move_lst:
                x, D = move_lst.pop(0)
                X = int(x)
        
    print(time)

