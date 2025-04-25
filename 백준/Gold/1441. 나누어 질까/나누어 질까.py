import sys
from math import gcd
input = sys.stdin.readline

def solve(A: list[int], L: int, R: int) -> int:
    n = len(A)
    ans = 0
    for mask in range(1, 1 << n):
        l = 1
        bits = mask.bit_count()
        overflow = False
        for i in range(n):
            if mask & (1 << i):
                ai = A[i]
                g = gcd(l, ai)
                mul = ai // g
                if l > R // mul:
                    overflow = True
                    break
                l *= mul
                if l > R:
                    overflow = True
                    break
        if overflow:
            continue
        cnt = R // l - (L - 1) // l
        if bits & 1:
            ans += cnt
        else:
            ans -= cnt
    return ans

def main():
    # 입력
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    # 풀이
    result = solve(A, L, R)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
