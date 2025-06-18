import sys
import math
input = sys.stdin.readline

def solve(n: int) -> int:
    r = int(math.isqrt(n))
    if r * r == n:
        return -1

    cnt = 0

    lim = int(math.isqrt(n // 2))
    for a in range(1, lim + 1):
        b2 = n - a*a
        b = int(math.isqrt(b2))
        if b >= a and b*b == b2:
            cnt += 1

    lim = int(math.isqrt(n))
    for u in range(1, lim + 1):
        if n % u: continue
        v = n // u
        if u < v and ((u ^ v) & 1) == 0:
            cnt += 1

    return cnt

def main():
    n = int(input().strip())
    print(solve(n))

if __name__ == "__main__":
    main()
