import sys, math
input = sys.stdin.readline

def solve(n: int) -> int:
    dp = [0] * (n + 1)
    dp[1] = 1
    facto = {}
    f = 1
    for k in range(1, 20):
        f *= k
        if f > n: break
        if k < f:
            facto[f] = k
    for x in range(2, n + 1):
        best = x
        half = x >> 1
        for i in range(1, half + 1):
            s_val = dp[i] + dp[x - i]
            if s_val < best:
                best = s_val
        r = int(math.isqrt(x))
        for d in range(2, r + 1):
            if x % d == 0:
                s_val = dp[d] + dp[x // d]
                if s_val < best:
                    best = s_val
        if x in facto:
            if dp[facto[x]] < best:
                best = dp[facto[x]]
        dp[x] = best
    return dp[n]

def main():
    # 입력
    n = int(input())
    
    # 풀이
    result = solve(n)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()

