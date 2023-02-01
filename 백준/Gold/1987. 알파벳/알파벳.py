import sys
input = sys.stdin.readline

R,C = map(int,input().split())
arr = [list(input()) for _ in range(R)]
visit = [1]*(26)
res = 0

def func(i,j,f):
    global res

    res = max(res,f)

    for d in [[1,0],[-1,0],[0,1],[0,-1]]:
        ni = i + d[0]
        nj = j + d[1]
        if 0 <= ni < R and 0 <= nj < C and visit[ord(arr[ni][nj])-65]:
            visit[ord(arr[ni][nj])-65] = 0
            func(ni,nj,f+1)
            visit[ord(arr[ni][nj])-65] = 1

visit[ord(arr[0][0])-65] = 0
func(0,0,1)
print(res)