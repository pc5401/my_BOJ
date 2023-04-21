import sys
input = sys.stdin.readline

def res(h:int,w:int, x:int,y:int):
    lst = [[0] * (w) for i in range(h)]

    for i in range(h):
        for j in range(w):
            if (x > 0 and 0 <= i < x) or (y > 0 and 0 <= j < y):
                lst[i][j] = arr[i][j]

            else:
                lst[i][j] = arr[i][j] - lst[i-x][j-y]

    return lst


if __name__ == "__main__":
    H,W,X,Y = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(H + X)]
    
    for r in res(H,W,X,Y):
        print(*r)
