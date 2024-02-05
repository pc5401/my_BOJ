import collections


def get_start(arr: list):
    for i in range(N):
            for j in range(M):
                if arr[i][j] == 'I':
                    return i, j


if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    start =get_start(arr)
    res = 0

    queue = collections.deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1

    while queue:
        x, y = queue.popleft()

        for d in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni = x + d[0]
            nj = y + d[1]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if arr[ni][nj] == 'P':
                    queue.append((ni, nj))
                    visited[ni][nj] = 1
                    res += 1
                elif arr[ni][nj] == 'O':
                    queue.append((ni, nj))
                    visited[ni][nj] = 1
                elif arr[ni][nj] == 'X':
                    visited[ni][nj] = 1
                else:
                    visited[ni][nj] = 1

    print(res if res else 'TT')