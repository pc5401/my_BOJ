import sys
input = sys.stdin.readline

def dragon(i: int, j: int, d:int, g: int):
    ni = i + delta[d][0]
    nj = j + delta[d][1]
    if 0 <= ni < 101 and 0 <= nj < 101:
        lst = [[i,j], [ni, nj]]
    else:
        arr[i][j] = 1
        return
    
    dir_lst = [d]
    
    for tc in range(g):
        dir_stack = dir_lst[:]
        while dir_stack:
            dir = (dir_stack.pop() + 1) % 4
            ni = ni + delta[dir][0]
            nj = nj + delta[dir][1]
            if 0 <= ni < 101 and 0 <= nj < 101:
                lst.append([ni,nj])
                dir_lst.append(dir)
            else:
                check(lst)
                return
    check(lst)


def check(dlst: list):
    for l in dlst:
        arr[l[0]][l[1]] = 1


def solve(arr: list) -> int:
    ans = 0
    for i in range(100):
        for j in range(100):
            cnt = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1]
            if cnt == 4:
                ans += 1
    return ans


if __name__ == '__main__':
    delta = [(0,1), (-1,0), (0, -1), (1, 0)]
    N = int(input())
    arr = [[0 for j in range(101)] for i in range(101)]
    for _ in range(N):
        X, Y, D, G = map(int,input().split())
        dragon(Y, X ,D, G)
    print(solve(arr))
