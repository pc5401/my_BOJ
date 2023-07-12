import sys
import collections
input = sys.stdin.readline


def bfs(arr: list, n: int, m: int) -> int:
    visit = [[0 for j in range(m)] for i in range(n)]
    Q = collections.deque()
    del_set = set()


    visit[0][0] = 1
    Q.append([0,0])

    while Q:
        v = Q.popleft()

        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]
            if 0 <= ni < n and 0<= nj < m:
                if arr[ni][nj]: # 1 이면
                    if visit[ni][nj] < 0:
                        del_set.add((ni,nj))
                    visit[ni][nj] -= 1

                else:
                    if not visit[ni][nj]:
                        Q.append([ni,nj])
                        visit[ni][nj] = 1

    for i,j in del_set:
        arr[i][j] = 0

    if del_set:
        return True
    else:
        return False


if __name__ == '__main__':
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for i in range(N)]
    res = 0
    
    while True:
        if bfs(arr, N, M):
            res += 1
            continue
        break
    
    print(res)