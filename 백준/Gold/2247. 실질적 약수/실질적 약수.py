import sys
input = sys.stdin.readline

def solve(n: int) -> int:
    mod = 10**6
    m = n
    M = m // 2
    ans = 0
    l = 2
    while l <= M:
        q = m // l
        r = m // q
        if r > M:
            r = M
        cnt = r - l + 1
        sum_d = cnt * (l + r) // 2
        ans += (q - 1) * sum_d
        l = r + 1
    return ans % mod

def main():
    # 입력
    n = int(input().strip())
    # 풀이
    result = solve(n)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
