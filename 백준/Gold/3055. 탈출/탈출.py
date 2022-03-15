from collections import deque

# BFS 로 풀자
# 고슴도치는 숫자로 이동 표시하면서 체크
# 물은 '*'로 계속 퍼트림
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

R, C = map(int, input().split())

wtr = []
arr = []
#  입력 값  비버굴 =target, 고슴도치 = 0 로 바꿈, 물은 리스트에 저장
for i in range(R):
    lst = list(input())

    for j in range(C):
        if lst[j] == 'D':
            target = [i, j]
        elif lst[j] == 'S':
            lst[j] = 0
            dochi = [i, j]
        elif lst[j] == '*':
            wtr.append([i, j])

    arr.append(lst)

# 고슴도치 먼저 큐, 다음로 물은 넣는다.
queue = deque()
queue.append(dochi)
for i in range(len(wtr)):
    queue.append(wtr[i])

# bfs
ans = 'KAKTUS'
while queue:

    if arr[target[0]][target[1]] != 'D':  # 탈출 조건
        ans = arr[target[0]][target[1]]
        break

    v = queue.popleft()

    if arr[v[0]][v[1]] == '*':  # 물 = '*'
        for d in delta:
            ni = v[0] + d[0]
            nj = v[1] + d[1]

            if 0 <= ni < R and 0 <= nj < C:
                if arr[ni][nj] == '.' or isinstance(arr[ni][nj], int):
                    arr[ni][nj] = '*'
                    queue.append([ni, nj])

    else:  # 고슴도치, '*' 아니면 다 숫자
        for d in delta:
            ni = v[0] + d[0]
            nj = v[1] + d[1]

            if 0 <= ni < R and 0 <= nj < C:
                if arr[ni][nj] == '.':
                    arr[ni][nj] = arr[v[0]][v[1]] + 1
                    queue.append([ni, nj])
                elif arr[ni][nj] == 'D':  #도착
                    arr[ni][nj] = arr[v[0]][v[1]] + 1
                    queue.append([ni, nj])
                    break
print(ans)