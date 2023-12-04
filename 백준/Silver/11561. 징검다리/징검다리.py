import sys
input = sys.stdin.readline


def solve(n):
    if n == 1 or n == 2:
        return 1
    
    lo, hi = 1, n
    
    while lo < hi:
        mid = (lo+hi) // 2
        v = mid * (mid+1) / 2

        if v <= n:
            lo = mid+1
        else:
            hi = mid
    
    return lo-1



if __name__ == "__main__":
    T = int(input())
    N = [int(input()) for _ in range(T)]
    for n in N:
        print(solve(n))
