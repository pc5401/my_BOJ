import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())

    lo, hi = 0, N // 2

    while lo < hi:
        mid = (lo + hi) // 2
        if mid*mid < N:
            lo = mid + 1
        else:
            hi = mid

    print(lo)