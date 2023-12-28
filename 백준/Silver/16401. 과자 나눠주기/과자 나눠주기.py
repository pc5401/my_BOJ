import sys
input = sys.stdin.readline

def snack_cnt(v: int) -> int:
    cnt = 0
    for i in lst:
        if i < v:
            continue
        cnt += i // v
    return cnt



if __name__ == "__main__":
    M, N = map(int, input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    
    lo, hi = 1, max(lst)

    while lo <= hi:
        mid = (lo+hi) // 2
        snack = snack_cnt(mid)
        if snack < M:
            hi = mid - 1
        else:
            lo = mid + 1
    
    print(hi)
