import sys
input = sys.stdin.readline


N, M = map(int,input().split())
sung = [list(input()) for _ in range(N)]
nlst = [1] * N
mlst = [1] * M

for i in range(N):
    for j in range(M):
        if sung[i][j] == 'X':
            nlst[i] = 0
            mlst[j] = 0

n = sum(nlst)
m = sum(mlst)
res = n+m-min(n,m)

print(res)
