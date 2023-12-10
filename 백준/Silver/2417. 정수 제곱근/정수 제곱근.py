import sys
input = sys.stdin.readline


def find(n: int):
    lo, hi = 0, n

    while lo < hi:
        mid = (lo+hi)//2
        if mid**2 < n:
            lo = mid + 1
        else:
            hi = mid
    
    return lo


if __name__ == "__main__":
    N = int(input())
    print(find(N))