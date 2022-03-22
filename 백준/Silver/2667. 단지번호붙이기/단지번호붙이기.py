from collections import deque

def numbering(start):
    global num
    num -= 1  # 음수로 번호붙이기
    cnt = 1  # 단지 수 계산

    grid[start[0]][start[1]] = num  # 들어온 값 바꾸기
    q = deque([start])

    while q:
        v = q.popleft()

        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  # 상하좌우
            ni = v[0] + d[0]
            nj = v[1] + d[1]

            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] == 1:
                    grid[ni][nj] = num
                    q.append([ni, nj])
                    cnt += 1

    return cnt

n = int(input())
grid = [list(map(int, input())) for _ in range(n)]

num = 0
ans = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            # numbering([i, j])
            ans.append(abs(numbering([i, j])))
ans.sort(reverse=False)
print(abs(num))
for a in ans:
    print(a)