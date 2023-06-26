import sys
input = sys.stdin.readline

def matrix(mat1: list, mat2: list):
    global N
    ans = [[0 for j in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            val = 0
            for k in range(N):
                val += mat1[i][k] * mat2[k][j]
            ans[i][j] = val % 1000
    
    return ans


def  div_conq(mat, n):
    if n == 1: # 기본
        return mat
    
    elif n % 2: # 홀수
        dived = div_conq(mat, (n-1) //2)
        return matrix(mat, matrix(dived, dived))
    
    else: # 짝수
        dived = div_conq(mat, n // 2)
        return matrix(dived, dived)

if __name__ == '__main__':
    N, K = map(int,input().split())
    base = [list(map(int,input().split())) for i in range(N)]
    res = div_conq(base, K)
    for r in res:
        print(*(val % 1000 for val in r))