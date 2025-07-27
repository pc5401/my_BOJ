import sys
input = sys.stdin.readline

def get_num(n: int) -> int:
    if n < 0:
        return 0
    res = 0
    p = 1  # 10^k
    while p <= n:
        high = n // (p * 10)
        curr = (n // p) % 10
        low = n % p

        res += high * p * 45
        res += (curr * (curr - 1) // 2) * p
        res += curr * (low + 1)
        p *= 10
    return res

def solve(L: int, U: int) -> int:
    return get_num(U) - get_num(L - 1)

def main():
    # 입력
    L, U = map(int, input().split())
    # 풀이
    ans = solve(L, U)
    # 출력
    print(ans)

if __name__ == "__main__":
    main()
