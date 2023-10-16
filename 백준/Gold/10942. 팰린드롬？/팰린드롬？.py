import sys
import heapq
input = sys.stdin.readline


def dp_table(N: int, lst: list) -> list:
    table = [[0]*N for _ in range(N)]
    
    for i in range(N):
        table[i][0] = 1
    if N == 1:
        return table
    
    for i in range(N-1):
        if lst[i] == lst[i+1]:
            table[i][1] = 1 
    
    for lenth in range(2, N):
        for i in range(N):
            if i+lenth >= N:
                continue
            if lst[i] == lst[i+lenth] and table[i+1][lenth-2] == 1:
                table[i][lenth] = 1

    return table


if __name__ == "__main__":
    # 입력 & 전처리
    N = int(input())
    lst = list(map(int, input().split()))
    M = int(input())
    qstn = [tuple(map(int, input().split())) for _ in range(M)]
    dp = dp_table(N, lst)
    res = []
    for S, E in qstn:
        res.append(dp[S-1][E-S])
    for r in res:
        print(r)

