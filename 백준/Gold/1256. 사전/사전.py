import sys
input = sys.stdin.readline


def get_dp() -> list[list[int]]:
    MAX_VAL = 10**9 + 1 
    dp = [[0]*201 for _ in range(201)]

    for i in range(201):
        dp[i][0] = 1
        for j in range(1, i+1):
            tmp = dp[i-1][j-1] + dp[i-1][j]
            if tmp > MAX_VAL:
                tmp = MAX_VAL
            dp[i][j] = tmp
    
    return dp


def solve(N: int, M: int, K: int) -> int | str:
    dp = get_dp()
    
    if dp[N+M][N] < K:
        return -1

    ans = []
    a_cnt = N
    z_cnt = M
    k = K

    while a_cnt > 0 and z_cnt > 0:
        left = dp[a_cnt + z_cnt - 1][a_cnt - 1]
        if left >= k:
            ans.append('a')
            a_cnt -= 1
        else:
            ans.append('z')
            z_cnt -= 1
            k -= left
    
    if a_cnt > 0:
        ans.append('a' * a_cnt)
    
    if z_cnt > 0:
        ans.append('z' * z_cnt)

    return "".join(ans)


def main():
    # 입력
    N, M, K = map(int, input().split())

    # 풀이
    result = solve(N, M, K)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
