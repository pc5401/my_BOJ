import sys
from math import gcd
input = sys.stdin.readline

def solve(N, A):
    p, q = 0, 1
    for a in A:
        p = p * a + q
        q = q * a
        g = gcd(p, q)
        p //= g
        q //= g
    num, den = q, p
    g = gcd(num, den)
    num //= g
    den //= g
    return f"{num}/{den}"

def main():
    # 입력
    N = int(input().strip())
    A = list(map(int, input().split()))

    # 풀이
    result = solve(N, A)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
