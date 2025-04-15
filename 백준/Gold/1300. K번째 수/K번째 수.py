import sys
input = sys.stdin.readline

def solve(N: int, k: int) -> int:
    lo = 0
    hi = N * N  # N^2 최대 값
    while lo < hi:
        mid = (lo + hi) // 2
        cnt = 0
        for i in range(1, N + 1):
            cnt += min(N, mid // i)
        if cnt >= k:
            hi = mid
        else:
            lo = mid + 1
    return lo

def main():
    # 입력
    N = int(input().strip())
    k = int(input().strip())
    
    # 풀이
    result = solve(N, k)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
