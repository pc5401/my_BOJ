def after(maps):
    lst = []  # 잠길 땅 체크
    for r in range(R):  # 전체 순회
        for c in range(C):
            if maps[r][c] == 'X':
                cnt = 0  # 3 이상은 50 년 뒤, 잠김
                for d in [[-1, 0],[1,0],[0,-1],[0,1]]: # 상하좌우
                    nr = r + d[0]
                    nc = c + d[1]
                    if nr < 0 or nr >= R or nc < 0 or nc >= C: # 범위 초과
                        cnt += 1
                    elif 0 <= nr < R and 0 <= nc < C and maps[nr][nc] == '.':
                        cnt += 1
                    else:
                        pass
                if cnt >= 3: # 3면 이상
                    lst.append([r, c])

    for i, j in lst: # 탐색 끝나고
        maps[i][j] = '.'  # 바다에 잠기기


def new(maps):
    startR = startC = 100
    endR = endC = 0

    for r in range(R):
        for c in range(C):
            if maps[r][c] == 'X':
                if startR > r:
                    startR = r
                if startC > c:
                    startC = c

                if endR < r:
                    endR = r
                if endC < c:
                    endC = c

    # print(startR, endR)
    # print(startC, endC)
    result = []
    for i in range(startR, endR + 1):
        result.append(maps[i][startC:endC+1])

    return result


R, C =map(int, input().split())
maps = [list(input()) for _ in range(R)]

after(maps)  # 섬 잠기기
res = new(maps)

for i in range(len(res)):
    print(''.join(res[i]))