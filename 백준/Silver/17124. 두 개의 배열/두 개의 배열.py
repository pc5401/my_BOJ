import sys
input = sys.stdin.readline


def get_val(target: int, m: int, lst: list[int]) -> int:
    lo, hi = 0, m

    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] >= target:
            hi = mid
        else:
            lo = mid + 1

    
    # 거리 같으면 작은 값 찾기
    pos = lo
    
    arr = []
    if pos > 0:
        arr.append(lst[pos - 1])
    if pos < len(lst):
        arr.append(lst[pos])
    
    best = None
    best_diff = float('inf')
    for val in arr:
        diff = abs(val - target)
        if diff < best_diff:
            best_diff = diff
            best = val
        elif diff == best_diff and val < best:
            best = val
    
    return best



def solve(n: int, m: int, A: list[int], B: list[int]) -> int:
    b = sorted(B)

    C = [get_val(A[i], m, b) for i in range(n)]
    
    return sum(C)

def main():
    # 입력값
    result = []
    T = int(input().strip())
    for _ in range(T):
        n, m  =map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        result.append(solve(n,m,A,B))
    
    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
