import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    arr.sort()
    res = 4
    
    for i in range(N): # start(=lo) 는 순차적으로
        lo = i
        hi = N-1
        while lo < hi:
            if arr[hi] - arr[lo] > 4:
                hi -= 1 # end(=hi) 값만 감소
            else:
                res = min(res, 4-(hi-lo))
                break

    print(res)


