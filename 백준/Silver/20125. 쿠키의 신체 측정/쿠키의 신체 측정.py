import sys
input = sys.stdin.readline


def look_for_heart(N: int, a: list) -> tuple:
    for i in range(N):
        for j in range(N):
            if a[i][j] == '*': # 머리
                return (i+1, j)


def length_of_bodys(N:int, a: list, heart:tuple) -> list:
    rtn = [0] * 5
    x, y = heart
    for j in range(y-1, -1, -1): # 왼팔
        if a[x][j] == '*':
            rtn[0] += 1
        else:
            break
    
    for j in range(y+1, N): # 오른팔
        if a[x][j] == '*':
            rtn[1] += 1
        else:
            break

    for i in range(x+1, N): # 허리
        if a[i][y] == '*':
            rtn[2] += 1
        else:
            left = (i, y-1)
            right = (i, y+1)
            break
    
    for i in range(left[0], N):
        if a[i][left[1]] == '*':
            rtn[3] += 1
        else:
            break
    
    for i in range(right[0], N):
        if a[i][right[1]] == '*':
            rtn[4] += 1
        else:
            break
    
    return rtn


if __name__ == '__main__':
    N = int(input())
    a = [list(input().rstrip()) for _ in range(N)]
    heart = look_for_heart(N, a)
    cookie = length_of_bodys(N, a, heart)
    print(heart[0]+1, heart[1]+1)
    print(*cookie)