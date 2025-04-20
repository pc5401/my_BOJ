import sys
input = sys.stdin.readline

def solve(N: int, K: int, C: list[int]) -> int:
    low, high = 0, sum(C) // K
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        # mid 그룹 확인
        total = sum(min(c, mid) for c in C)
        if total >= mid * K:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

def main():
    # 입력
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    # 풀이
    result = solve(N, K, C)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
