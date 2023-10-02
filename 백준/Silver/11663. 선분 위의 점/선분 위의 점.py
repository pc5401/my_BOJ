import sys
input = sys.stdin.readline

def upper_index(n: int, target: int, points: list)->int:
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if points[mid] <= target: 
            lo = mid + 1
        else: 
            hi = mid
    
    return lo

def lower_index(n: int, target: int, points: list)->int:
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if points[mid] < target: 
            lo = mid + 1
        else: 
            hi = mid
    
    return lo

if __name__ == "__main__":
    # 입력 & 전처리
    N, M = map(int, input().split())
    points = list(map(int, input().split()))
    points.sort()
    for _ in range(M):
        left, right = map(int, input().split())
        print(upper_index(N, right, points) - lower_index(N, left, points))

