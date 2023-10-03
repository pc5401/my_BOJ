import sys
import collections
input = sys.stdin.readline

def turn(r:int, c:int, Length: int, A: list): # 재귀
    if Length <= 1:
        return

    L_len = Length-1
    for i in range(L_len):
        temp = A[r][c+i]
        A[r][c+i] = A[r-i + L_len][c]
        A[r-i + L_len][c] = A[r+L_len][c+L_len-i]
        A[r+L_len][c+L_len-i] = A[r+i][c+L_len]
        A[r+i][c+L_len]= temp
    
    turn(r+1, c+1, Length-2, A)

def melt(n: int, A: list) -> list:
    new_A = [[0]*(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not A[i][j]: # 얼음 없는 곳은 pass
                continue
            cnt = 0
            for d in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < n and 0 <= nj < n and A[ni][nj]:
                    cnt += 1
            
            if cnt < 3:
                new_A[i][j] = A[i][j] - 1
            else:
                new_A[i][j] = A[i][j]

    return new_A


def bfs(i: int, j: int, n: int, A: list, visited: list) -> int:
    Q = collections.deque()
    Q.append([i,j])
    visited[i][j] = 1
    size = 0

    while Q:
        v = Q.popleft()
        size += 1
        for d in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]
            if 0 <= ni < n and 0 <= nj < n:
                if not visited[ni][nj] and A[ni][nj]:
                    visited[ni][nj] = 1
                    Q.append([ni, nj])

    return size


def check_ice_size(n: int, A: list) -> int:
    visited = [[0]*(n) for _ in range(n)]
    maxV = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and A[i][j]:
                maxV = max(bfs(i, j, n, A, visited), maxV)

    return maxV


def solve(N:int, Q:int, A:list, L:list) -> tuple:
    n = 2**N
    for q in range(Q):
        l = L[q]

        for r in range(0, n, 2**l):
            for c in range(0, n, 2**l):
                turn(r, c,2**l, A)
        # 얼음 녺이기
        A = melt(n, A)
    total_ice = sum([sum(A[i]) for i in range(n)])
    ice_size = check_ice_size(n, A)

    return total_ice, ice_size


if __name__ == "__main__":
    # 입력 & 전처리
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2**N)]
    L = list(map(int, input().split()))
    total_ice_cnt, most_ice_size = solve(N, Q, A, L)
    print(total_ice_cnt)
    print(most_ice_size)

