from typing import List


def make_sum_table(N: int, M: int, arr: List[int]):    
    dp = [[0]*(M+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

    return dp


def calculator(i: int, j: int, x: int, y: int, sum_table: List[int]):
    a = sum_table[x][y]
    b = sum_table[x][j-1]
    c = sum_table[i-1][y]
    d = sum_table[i-1][j-1]
    return a - b - c + d


def main():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    K = int(input())
    target_ranges = [list(map(int, input().split())) for _ in range(K)]
    
    sum_table = make_sum_table(N, M, arr)
    res = []
    
    for target_range in target_ranges:
        res.append(calculator(*target_range, sum_table))

    for r in res:
        print(r)

if __name__ == "__main__":
    main()