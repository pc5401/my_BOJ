import sys
input = sys.stdin.readline


def garo(i,j):
    global M
    visit[i][j] = 1
    if j+1 < M and arr[i][j+1] == '-':
        garo(i,j+1)
    return

def sero(i,j):
    global N
    visit[i][j] = 1
    if i+1 < N and arr[i+1][j] == '|':
        sero(i+1,j)
    return


N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
res =0

for n in range(N):
    for m in range(M):
        if visit[n][m]:
            continue
        
        res += 1
        if arr[n][m] == '-':
            garo(n,m)

        if arr[n][m] == '|':
            sero(n,m)

print(res)