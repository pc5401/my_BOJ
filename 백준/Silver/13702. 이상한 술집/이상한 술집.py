import sys
input = sys.stdin.readline

def cnt_kettle(ml: int, kettle:list) -> int:
    cnt = 0
    for k in kettle:
        cnt += (k // ml)
    return cnt

if __name__ == "__main__":
    N, K = map(int, input().split())
    kettle = [ int(input()) for _ in range(N)]
    
    lo, hi = 1, max(kettle)+1

    while lo < hi:
        mid = (lo+hi) // 2

        if cnt_kettle(mid, kettle) < K:
            hi = mid
        else:
            lo = mid + 1
    
    print(hi - 1)