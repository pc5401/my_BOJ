import sys
from math import gcd, isqrt

def solve(G, L):
    if L % G != 0:
        return None
    n = L // G
    best_sum = None
    best_pair = None

    r = isqrt(n)
    for d in range(1, r + 1):
        if n % d != 0:
            continue
        e = n // d
        if gcd(d, e) != 1:
            continue
        a, b = G * d, G * e
        s = a + b
        if best_sum is None or s < best_sum:
            best_sum = s
            best_pair = (min(a, b), max(a, b))
    return best_pair

def main():
    data = sys.stdin.read().strip().split()
    # 입력
    G, L = map(int, data[:2])
    # 풀이
    ans = solve(G, L)
    # 출력
    if ans is None:
        print(-1)
    else:
        print(ans[0], ans[1])

if __name__ == "__main__":
    main()
