import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    stacked_A = [0]
    for i in range(N):
        stacked_A.append(stacked_A[-1] + A[i])
    

    # 투 포인터
    lo, hi = 0, 1
    res = 0
    while lo <= hi and hi <= N:
        sumV = stacked_A[hi] - stacked_A[lo]
        if sumV < M:
            hi += 1
        elif sumV > M:
            lo += 1
        else:
            hi += 1
            res += 1

    print(res)
