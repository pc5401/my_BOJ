import sys
from functools import lru_cache
input = sys.stdin.readline

def solve(N, R, G, B):
    maxk = N
    fact = [1] * (maxk + 1)
    for i in range(2, maxk + 1):
        fact[i] = fact[i-1] * i

    def nCk(n, k):
        if k < 0 or k > n: return 0
        return fact[n] // (fact[k] * fact[n-k])

    @lru_cache(None)
    def dp(level, r, g, b):
        if level > N:
            return 1
        ans = 0
        if r >= level:
            ans += dp(level + 1, r - level, g, b)
        if g >= level:
            ans += dp(level + 1, r, g - level, b)
        if b >= level:
            ans += dp(level + 1, r, g, b - level)
        if level % 2 == 0:
            half = level // 2
            ways = nCk(level, half)
            if r >= half and g >= half:
                ans += ways * dp(level + 1, r - half, g - half, b)
            if r >= half and b >= half:
                ans += ways * dp(level + 1, r - half, g, b - half)
            if g >= half and b >= half:
                ans += ways * dp(level + 1, r, g - half, b - half)
        if level % 3 == 0:
            third = level // 3
            ways = fact[level] // (fact[third] * fact[third] * fact[third])
            if r >= third and g >= third and b >= third:
                ans += ways * dp(level + 1, r - third, g - third, b - third)
        return ans

    return dp(1, R, G, B)

def main():
    # 입력
    N, R, G, B = map(int, input().split())

    # 풀이
    result = solve(N, R, G, B)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
