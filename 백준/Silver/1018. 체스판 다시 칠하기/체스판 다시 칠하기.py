import sys
input = sys.stdin.readline

def paint(x,y):
    w = 0
    b = 0
    for i in range(x,x+8):
        for j in range(y, y+8):

            if arr[i][j] != B[i%2][j-y]:
                b += 1

            if arr[i][j] != W[i%2][j-y]:
                w += 1

    return min(b,w)

if __name__ == "__main__":
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    res = 65
    B = [['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]
    W = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]

    for i in range(N-7):
        for j in range(M-7):
            res = min(res, paint(i,j))

    print(res)