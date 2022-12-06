N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N) ]
res = 0

def func(n):
    global N,M

    v = 0
    if n == 1:
        return 1
    
    for i in range(N-n+1):
        for j in range(M-n+1):
            if arr[i][j] == arr[i+n-1][j] and arr[i][j] == arr[i][j+n-1] and arr[i][j] == arr[i+n-1][j+n-1]:
                v = n ** 2
                return v
    return v


l = min(N,M)
res = 0

for _ in range(l,0,-1):
    
    res = func(_)
    if res:
        break

print(res)
        

