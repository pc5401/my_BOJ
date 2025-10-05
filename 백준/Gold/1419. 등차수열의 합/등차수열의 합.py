import sys
from math import gcd
input = sys.stdin.readline

def solve(l, r, k):
    A = k
    B = k * (k - 1) // 2
    g = gcd(A, B)
    a = A // g
    b = B // g
    F = a * b - a - b
    S0 = A + B + g * (F + 1)
    target = (A + B) % g

    ans = 0
    L = max(l, S0)
    if L <= r:
        first = L + ((target - L) % g)
        if first <= r:
            ans += (r - first) // g + 1

    hi = min(r, S0 - 1)
    if l <= hi:
        start = max(l, A + B)
        if start <= hi:
            s = start + ((target - start) % g)
            while s <= hi:
                n = (s - (A + B)) // g
                ok = False
                t = 0
                while b * t <= n:
                    if (n - b * t) % a == 0:
                        ok = True
                        break
                    t += 1
                if ok:
                    ans += 1
                s += g

    return ans

def main():
    # 입력
    l = int(input().strip())
    r = int(input().strip())
    k = int(input().strip())

    # 풀이
    result = solve(l, r, k)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
