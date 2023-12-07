import sys
input = sys.stdin.readline


def solve(target) -> int:
    global N

    lo, hi = 0, N-1

    while lo < hi:
        mid = (lo + hi) // 2
        
        if A[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    
    if A[lo] == target:
        return 1
    else:
        return 0


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    lst = list(map(int, input().split()))
    A.sort()
    result = []

    for target in lst:
        result.append(solve(target))

    for res in result:
        print(res)