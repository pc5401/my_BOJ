from collections import deque

N, M, t = map(int, input().split())  # 시간, 세로 ,가로
# 0 : 빈 공간, 1 : 벽, 2 : 그람, (n,m) 공주 좌표
n, m = N-1, M-1

grid = []
for i in range(N):  # 검 찾기
    lst = list(map(int, input().split()))
    for j in range(M):
        if lst[j] == 2:
            sord = [i, j]
    grid.append(lst)


minV = 100000

def BFS(target):  # 목적지 입력 그람(전설의 검) or 공주
    arr = [[ 0 for i in range(M)] for j in range(N)]
    queue = deque([])
    queue.append([0, 0])
    visited =[[0, 0]]

    while queue:

        v = queue.popleft()

        if arr[v[0]][v[1]] >= minV:
            return -10


        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]

            if 0 <= ni < N and 0 <= nj < M:  # 범위 지정
                if (grid[ni][nj] == 0 or grid[ni][nj] == 2) and not [ni, nj] in visited:  # 길, 전설의 검(2)도 길임
                    arr[ni][nj] = arr[v[0]][v[1]] + 1
                    queue.append([ni, nj])
                    visited.append([ni, nj])

                if ni == target[0] and nj == target[1]:  # 목적지 도착
                    return arr[v[0]][v[1]] + 1


    # 목적지를 못 갔다.
    return -1

# 검을 찾아 보자.
S_dst = BFS(sord)

if S_dst > 0:  # -1 이 아니면
    minV = S_dst + (abs(sord[0] - n) + abs(sord[1] - m))

if sord == [0, 0]:  # 시작하자 마자 검 취득
    minV = (abs(sord[0] - n) + abs(sord[1] - m))


# 공주를 찾아 보자
prin_dst = BFS([n, m])

if prin_dst == -10:  # 검이 더 빠른 경우
    ans = minV
elif prin_dst == - 1:  # 공주한테 가는 길에 벽이 있다.
    if t >= minV:  # 근데 검을 찾아서 공주한테 갈 수 있는 경우
        ans = minV
    else:
        ans = t*2  # Fail
else:  # 검X, 찾긴 함
    ans = prin_dst

res = ans if t - ans >= 0 else 'Fail'
print(res)