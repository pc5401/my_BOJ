import sys
input = sys.stdin.readline

def white(i, a, b, ni, nj):
    idx = data[a][b].index(i)
    lst = data[a][b][idx:]
    data[ni][nj].extend(lst)
    data[a][b] = data[a][b][:idx]

    for l in lst:
        pieces[l][1], pieces[l][2] = ni, nj


def red(i, a, b, ni, nj):
    lst = []
    v = data[a][b].pop()
    lst.append(v)

    while v != i:
        v = data[a][b].pop()
        lst.append(v)

    data[ni][nj].extend(lst)

    for l in lst:
        pieces[l][1], pieces[l][2] = ni, nj



def blue(i, a, b, c, n):
    if c == 1 : c = 0
    elif c == 0 : c = 1
    elif c == 2 : c = 3
    elif c == 3 : c = 2

    pieces[i][3] = c
    
    ni = a + delta[c][0]
    nj = b + delta[c][1]


    if 0 <= ni < n and 0 <= nj < n:
        if board[ni][nj] == 0: # 흰색 보드
            white(i, a, b, ni, nj)
            if len(data[ni][nj]) > 3:
                return True
                
        elif board[ni][nj] == 1: # 빨강
            red(i, a, b, ni, nj)
            if len(data[ni][nj]) > 3:
                return True
            
        elif board[ni][nj] == 2:  # 파랑
                return False
    else:  # 체스판 벗어나는 경우
        return False


def turn(n: int, k: int):
    for piece in pieces:
        i, a, b, c = piece
        ni = a + delta[c][0]
        nj = b + delta[c][1]

        if 0 <= ni < n and 0 <= nj < n:
            if board[ni][nj] == 0: # 흰색 보드
                white(i, a, b, ni, nj)
                if len(data[ni][nj]) > 3:
                    return True
                
            elif board[ni][nj] == 1: # 빨강
                red(i, a, b, ni, nj)
                if len(data[ni][nj]) > 3:
                    return True
                
            elif board[ni][nj] == 2: # 파랑
                if blue(i, a, b, c, n):
                    return True
            
        else: # 체스판 벗어나는 경우
            if blue(i, a, b, c, n): # 사실상 파랑
                return True
    
    return False



if __name__ == '__main__':
    N, K = map(int,input().split())
    board = [ list(map(int,input().split())) for _ in range(N) ]
    pieces = [[i, a - 1, b - 1, c - 1 ] for i, (a, b, c) in enumerate((map(int, input().split()) for _ in range(K)))]
    data = [[[] for j in range(N)] for i in range(N)]
    delta =[[0,1],[0,-1],[-1,0],[1,0]]

    for piece in pieces:
        i, a, b, c = piece
        data[a][b].append(i)

    T = 0
    while T <= 1000:
        T += 1
        if turn(N, K):
            break

    print(-1 if T > 1000 else T)
