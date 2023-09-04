import sys
import collections
input = sys.stdin.readline

def R_func(n: int,m: int, A: list) -> int:
    col = m

    arr = []
    for i in range(n):
        lst = []
        cnt = collections.Counter(A[i])
        for key in cnt.keys():
            if key > 0:
                lst.append([key, cnt[key]])

        lst.sort(key=lambda x: (x[1], x[0]))
        arr.append(sum(lst, [])) # flatten
        col = max(col, len(arr[i]))
    
    # 0 채우기
    new_A = [[0]*col for _ in range(n)]
    for i in range(n):
        for j in range(len(arr[i])):
            new_A[i][j] = arr[i][j]

    return new_A, col


def C_func(n: int,m: int, A: list) -> int:
    row = n

    arr = []
    for j in range(m):
        col_lst = [A[i][j] for i in range(n)] # 세로
        lst = []
        cnt = collections.Counter(col_lst)
        for key in cnt.keys():
            if key > 0:
                lst.append([key, cnt[key]])
        
        lst.sort(key=lambda x: (x[1], x[0]))
        arr.append(sum(lst, [])) # flatten
        row = max(row, len(arr[j]))

    new_A = [[0]*m for _ in range(row)]

    for j in range(m):
        for i in range(len(arr[j])):
            new_A[i][j] = arr[j][i]

    return new_A, row

if __name__ == '__main__':
    # 입력값 초기값 계산
    r, c, k = map(int, input().split())
    A = [list(map(int,input().split())) for _ in range(3)]
    N, M = 3, 3
    res = 0
    while res < 101:
        
        if r <= N and c <= M and A[r-1][c-1] == k:
            break

        if N >= M:
            A, M = R_func(N, M, A)
        else:
            A, N = C_func(N, M, A)


        res += 1

    print(res if res < 101 else -1)