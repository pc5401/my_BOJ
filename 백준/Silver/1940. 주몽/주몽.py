import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    res = 0

    lo, hi = 0, N-1

    while lo < hi:
        value = lst[lo] + lst[hi]
        if value == M:
            hi -= 1
            lo += 1
            res += 1
        
        elif value < M:
            lo += 1
        
        else:
            hi -= 1
    
    print(res)