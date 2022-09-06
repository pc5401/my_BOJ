from pprint import pprint

def left(i, j):
    ni = i -1
    nj = j -1

    while 0 <= ni < N and 0 <= nj < N:
        if arr[ni][nj]:
            return False
        
        ni -= 1
        nj -= 1

    return True


def right(i, j):
    ni = i -1
    nj = j +1

    while 0 <= ni < N and 0 <= nj < N:
        if arr[ni][nj]:
            return False
        
        ni -= 1
        nj += 1

    return True


def NQ(i):
    global res, N
    
    if i == N:
        res += 1
        # pprint(arr)
        return

    for j in range(N):
        check = True

        for y in range(i,-1,-1):
            if arr[y][j]:
                check = False
                break
        
        if not check:
            continue

        check = left(i, j)
        if not check:
            continue
        
        check = right(i, j)
        if check:
            arr[i][j] = 1
            NQ(i+1)
            arr[i][j] = 0


N = int(input())
arr = [[0]*N for _ in range(N)]
res = 0
NQ(0)
print(res)