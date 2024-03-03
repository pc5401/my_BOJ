import sys
input = sys.stdin.readline

def dfs(i: int, j: int, cnt: int, val: int):
    global res, N, e, w, n, s

    if cnt > N:
        res += val
        return

    if e and visited[i][j+1] == 0:
        visited[i][j+1] = 1
        dfs(i, j+1, cnt+1, val * (e*0.01))
        visited[i][j+1] = 0

    if w and visited[i][j-1] == 0:
        visited[i][j-1] = 1
        dfs(i, j-1, cnt+1, val * (w*0.01))
        visited[i][j-1] = 0
    
    if n and visited[i-1][j] == 0:
        visited[i-1][j] = 1
        dfs(i-1, j, cnt+1, val * (n*0.01))
        visited[i-1][j] = 0

    if s and visited[i+1][j] == 0:
        visited[i+1][j] = 1
        dfs(i+1, j, cnt+1, val * (s*0.01))
        visited[i+1][j] = 0

if __name__ == '__main__':
    # 입력값
    N, e, w, n, s = map(int, input().split())
    visited = [[0] * 31 for _ in range(31)]

    res = 0.0
    dfs(15, 15, 0, 1.0)
    print(res)

