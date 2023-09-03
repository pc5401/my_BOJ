import sys
import itertools
input = sys.stdin.readline

def range_start_end(move: int, n: int) -> tuple:

    if move == 0: # 상
        return 0, n, 0, n, 1, 1
    elif move == 1: # 하
        return n-1, -1, 0, n, -1, 1
    elif move == 2: # 좌
        return 0, n, 0, n, 1, 1
    elif move == 3: # 우
        return 0, n, n-1, -1, 1, -1
    

def block_sliding(i: int, j: int, n: int, dir: list, board: list, combined:list):
    
    ni = i + dir[0]
    nj = j + dir[1]
    if 0 <= ni < n and 0 <= nj < n:
        if board[ni][nj] == board[i][j] and not [ni, nj] in combined: # 결합
            board[ni][nj] *= 2
            board[i][j] = 0
            combined.append([ni,nj])

        elif board[ni][nj] == 0: # 이동
            board[ni][nj] = board[i][j]
            board[i][j] = 0
            block_sliding(ni, nj, n, dir, board, combined)


def eazy_2048(n: int, movements: list, board: list) -> int:

    for move in movements:
        combined = []
        i_start, i_end, j_start, j_end, idx, jdx = range_start_end(move, n)

        if move < 2: # 상하
            for i in range(i_start, i_end, idx):
                for j in range(j_start, j_end, jdx):
                    if board[i][j]:
                        block_sliding(i, j, n, delta[move], board, combined)
        
        else: # 좌우
            for j in range(j_start, j_end, jdx):
                for i in range(i_start, i_end, idx):
                    if board[i][j]:
                        block_sliding(i, j, n, delta[move], board, combined)

    rtn = 0
    for b in board:
        rtn = max(rtn, max(b))

    return rtn


if __name__ == '__main__':
    # 입력값 초기값 계산
    N = int(input())
    input_borad = [list(map(int,input().split())) for _ in range(N)]
    result = 0

    delta = [[-1,0],[1,0],[0,-1],[0,1]]
    for movements in itertools.product(range(4), repeat=5):
        result = max(result, eazy_2048(N, movements, [input_borad[i][:] for i in range(N)]))

    print(result)