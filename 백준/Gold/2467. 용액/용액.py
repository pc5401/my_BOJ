import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    minV = float('INF')
    res = []
    
    lo, hi = 0, N-1

    while lo < hi:
        val = lst[lo] + lst[hi]
        abs_val = abs(val)

        if abs_val < minV:
            minV = abs_val
            res = [lst[lo], lst[hi]]

        if val == 0:
            res = [lst[lo], lst[hi]]
            break
        elif val > 0:
            hi -= 1
        else:
            lo += 1
    
    print(*res)