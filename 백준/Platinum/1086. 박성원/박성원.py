import sys
from math import gcd
input = sys.stdin.readline

def solve(N, nums, K):
    lens = [len(s) for s in nums]
    max_len = max(lens) if N else 0

    pow10 = [1 % K]
    for _ in range(1, max_len + 1):
        pow10.append((pow10[-1] * 10) % K)

    rem = []
    for s in nums:
        r = 0
        for ch in s.strip():
            r = (r * 10 + (ord(ch) - 48)) % K
        rem.append(r)

    tenpow = [pow10[l] for l in lens]

    trans = [[0] * K for _ in range(N)]
    for j in range(N):
        tp = tenpow[j]
        rj = rem[j]
        for r in range(K):
            trans[j][r] = (r * tp + rj) % K

    size = 1 << N
    dp = [[0] * K for _ in range(size)]
    dp[0][0] = 1

    for mask in range(size):
        row = dp[mask]
        for r in range(K):
            val = row[r]
            if not val:
                continue
            m = mask
            for j in range(N):
                if not (m >> j) & 1:
                    nm = mask | (1 << j)
                    nr = trans[j][r]
                    dp[nm][nr] += val

    p = dp[size - 1][0]
    q = 1
    for i in range(2, N + 1):
        q *= i

    if p == 0:
        return "0/1"
    if p == q:
        return "1/1"
    g = gcd(p, q)
    return f"{p // g}/{q // g}"

def main():
    # 입력
    N = int(input())
    nums = [input().strip() for _ in range(N)]
    K = int(input())

    # 풀이
    result = solve(N, nums, K)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
