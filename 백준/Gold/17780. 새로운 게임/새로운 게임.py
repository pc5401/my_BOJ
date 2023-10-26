import sys
input = sys.stdin.readline


def cnt_piece(x:int, y: int, lst: list) -> int:
    cnt = 1
    fst = lst[0]
    piece_data[fst][1] = x
    piece_data[fst][2] = y
    for i in lst[1:]:
        cnt += 1
        piece_data[i][0] = 0
        piece_data[i][1] = x
        piece_data[i][2] = y

    return cnt

def move_piece(k: int, N: int, flag: bool):
    state, r, c, d = piece_data[k]
    ni, nj = r + delta[d][0], c + delta[d][1]

    if 0 <= ni < N and 0 <= nj < N:
        if color_table[ni][nj] == 0: #흰색
            while piece_table[r][c]:
                v = piece_table[r][c].pop(0)
                piece_table[ni][nj].append(v)
            if piece_table[ni][nj][0] != k:
                piece_data[k][0] = 0
            return cnt_piece(ni, nj, piece_table[ni][nj])
        
        elif color_table[ni][nj] == 1: #빨강
            while piece_table[r][c]:
                v = piece_table[r][c].pop()
                piece_table[ni][nj].append(v)
            if piece_table[ni][nj][0] != k:
                piece_data[k][0] = 0
                num = piece_table[ni][nj][0]
                piece_data[num][0] = 1
            return cnt_piece(ni, nj, piece_table[ni][nj])

        elif color_table[ni][nj] == 2: #파랑
            if d == 0: piece_data[k][3] = 1
            elif d == 1: piece_data[k][3] = 0
            elif d == 2: piece_data[k][3] = 3
            elif d == 3: piece_data[k][3] =2

            if flag:
                return 0
            return move_piece(k, N, 1)
    else:
        if d == 0: piece_data[k][3] = 1
        elif d == 1: piece_data[k][3] = 0
        elif d == 2: piece_data[k][3] = 3
        elif d == 3: piece_data[k][3] = 2

        if flag:
            return 0
        return move_piece(k, N, 1)



def solve(N: int, K: int) -> bool:
    for k in range(K):
        if piece_data[k][0]:
            m = move_piece(k, N, 0)
            if m > 3:
                return 1
    return 0

if __name__ == "__main__":
    N, K = map(int, input().split())
    delta = [(0,1),(0,-1),(-1,0),(1,0)]
    color_table = [list(map(int, input().split())) for _ in range(N)]
    piece_table = [[ [] for i in range(N)] for j in range(N)]
    piece_data = []
    for k in range(K):
        r,c,d = map(int, input().split())
        piece_table[r-1][c-1].append(k)
        piece_data.append([1,r-1,c-1,d-1])
    
    result = -1
    for tc in range(1, 1001):
        if solve(N, K):
            result = tc
            break

    print(result)