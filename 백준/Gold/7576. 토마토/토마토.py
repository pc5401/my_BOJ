import sys
import collections
input = sys.stdin.readline

def start_tomato(M, N) -> tuple:
    rtn = []
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                rtn.append((i,j))
    return rtn

def ans(M, N) -> int:
    maxV = 1

    for i in range(N):
        for j in range(M):
            if tomato[i][j] > maxV:
                maxV = tomato[i][j]
            
            if tomato[i][j] == 0:
                return -1
    
    return maxV - 1


if __name__ == "__main__":
    M, N = map(int, input().split())
    tomato = [list(map(int, input().split())) for _ in range(N)]
    
    Q = collections.deque()
    Q.extend(start_tomato(M, N))

    while Q:
        v = Q.popleft()
        for d in [(0,1),(1,0),(-1,0),(0,-1)]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]
            if 0 <= ni < N and 0 <= nj < M and tomato[ni][nj] == 0:
                tomato[ni][nj] = tomato[v[0]][v[1]] + 1
                Q.append((ni, nj))
    
    print(ans(M, N))