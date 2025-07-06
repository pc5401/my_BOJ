import sys
input = sys.stdin.readline
MOD = 10**9+7

def solve(N: int, K: int) -> int:
    modK = K if K > 0 else 1
    dp = [[[0]*2 for _ in range(2)] for _ in range(modK)]
    dp[0][0][0] = 1

    for _ in range(N):
        ndp = [[[0]*2 for _ in range(2)] for _ in range(modK)]
        for a_mod in range(modK):
            for last_b in (0,1):
                for has_c in (0,1):
                    cnt = dp[a_mod][last_b][has_c]
                    if not cnt:
                        continue
                    # A(K>0일 때만)
                    if K > 0:
                        nm = (a_mod + 1) % K
                        ndp[nm][0][has_c] = (ndp[nm][0][has_c] + cnt) % MOD
                    # B(연속 금지)
                    if last_b == 0:
                        ndp[a_mod][1][has_c] = (ndp[a_mod][1][has_c] + cnt) % MOD
                    # C
                    ndp[a_mod][0][1] = (ndp[a_mod][0][1] + cnt) % MOD
        dp = ndp

    res = 0
    for last_b in (0,1):
        res = (res + dp[0][last_b][1]) % MOD
    return res

def main():
    # 입력
    N, K = map(int, input().split())
    # 풀이
    result = solve(N, K)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
