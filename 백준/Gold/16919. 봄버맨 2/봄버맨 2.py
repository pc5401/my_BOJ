R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]


bombs = []
bomb_3 = [['O'] * C for r in range(R)]  # 전부 'O'으로 채움
bomb_1 = [['O'] * C for r in range(R)]  # 전부 'O'으로 채움


for r in range(R):
    for c in range(C):
        if arr[r][c] == 'O':
            bombs.append([r,c])


if N % 2==0:  
    for i in range(R):
        print('O'*C)

elif N == 1:
    for r in range(R):
        print(*arr[r], sep='')


else:
    for b in bombs:
        for d in [[1,0],[-1,0],[0,1],[0,-1],[0,0]]:
            ni = b[0] +d[0]
            nj = b[1] +d[1]
            if 0 <= ni < R and 0 <= nj < C:
                bomb_3[ni][nj] = '.'

    bomb = []

    for r in range(R):
        for c in range(C):
            if bomb_3[r][c] == 'O':
                bomb.append([r,c])

    for b in bomb:
        for d in [[1,0],[-1,0],[0,1],[0,-1], [0,0]]:
            ni = b[0] +d[0]
            nj = b[1] +d[1]
            if 0 <= ni < R and 0 <= nj < C:
                bomb_1[ni][nj] = '.'



    
    if N % 4 == 3:
        for r in range(R):
            print(*bomb_3[r], sep='')
    else:
        for r in range(R):
            print(*bomb_1[r], sep='')
