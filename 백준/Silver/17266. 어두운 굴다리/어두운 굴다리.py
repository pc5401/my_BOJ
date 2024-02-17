import sys
input = sys.stdin.readline


def is_possible(n: int, m: int, r: int, x_lst: list) -> bool:
    light = 0
    for x in x_lst:
        if light >= x-r:
            light = x+r
        else:
            return False
    return True if light >= N else False

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    x_lst = list(map(int, input().split()))
    res = 0
    
    lo, hi = 1, N+1
    while lo <= hi:
        mid = (lo+hi) // 2
        if is_possible(N, M, mid, x_lst):
            hi = mid - 1
        else:
            lo = mid + 1
    
    print(lo)