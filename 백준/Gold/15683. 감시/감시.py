import sys

input = sys.stdin.readline

def drawing(x, y, dir, fld):
    global N, M

    i, j = x + delta[dir][0], y + delta[dir][1]
    while 0 <= i < N and 0 <= j < M:
        if arr[i][j] == 6:  # 벽을 만났을 경우
            break
        if arr[i][j] == 0:
            fld[i][j] = 7  # CCTV가 볼 수 있는 위치를 7로 표시
        i += delta[dir][0]
        j += delta[dir][1]

def draw():
    global N, M

    field = [[arr[i][j] for j in range(M)] for i in range(N)]
    for i, j, d in cctv:
        if arr[i][j] == 1:
            drawing(i, j, d, field)
        elif arr[i][j] == 2:
            drawing(i, j, d, field)
            drawing(i, j, (d+2) % 4, field)
        elif arr[i][j] == 3:
            drawing(i, j, d, field)
            drawing(i, j, (d+1) % 4, field)
        elif arr[i][j] == 4:
            drawing(i, j, d, field)
            drawing(i, j, (d+1) % 4, field)
            drawing(i, j, (d+2) % 4, field)
        elif arr[i][j] == 5:
            drawing(i, j, d, field)
            drawing(i, j, (d+1) % 4, field)
            drawing(i, j, (d+2) % 4, field)
            drawing(i, j, (d+3) % 4, field)

    count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 0:
                count += 1

    return count

def func(idx):
    global res
    if idx == len(cctv):
        res = min(res, draw())
        return

    x, y, _ = cctv[idx]
    for d in range(4):
        cctv[idx][2] = d
        func(idx + 1)

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = []
    res = float('inf')
    cctv = []
    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            if 0 < row[j] < 6:
                cctv.append([i, j, 0])
        arr.append(row)

    func(0)
    print(res)