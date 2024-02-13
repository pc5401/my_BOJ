import sys
import math
input = sys.stdin.readline

def cal(target: int, n:int, m: int, l: int, lst:list) -> int:
    cnt = 0 
    for dist in lst:
        if dist <= target:
            continue
        cnt += (dist - 1) // target

    return cnt <= m


def solve(n:int, m: int, l: int, roads:list) -> int:
    lst = [roads[i] - roads[i-1] if i > 0 else roads[0] for i in range(n)]
    if roads[-1] != l:
        lst.append(l-roads[-1])
    lst.sort()
    N = len(lst)
    lo, hi = 1, l

    while lo <= hi:
        mid = (lo+hi) // 2
        if cal(mid, N, m, l, lst):
            hi = mid - 1
        else:
            lo = mid + 1
    
    return lo


if __name__ == '__main__':
    N, M, L = map(int, input().split())
    if N:
        roads = list(map(int, input().split()))
        roads.sort()
        print(solve(N, M, L, roads))
    else:
        print(L // (M+1) + 1 if L % (M+1) else L // (M+1))