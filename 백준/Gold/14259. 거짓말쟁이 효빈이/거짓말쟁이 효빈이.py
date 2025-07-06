import sys
input = sys.stdin.readline

def can_place(n: int, k: int, a: int, missiles: list[int], mid: int) -> bool:
    attacked = [False] * (n + 1)
    for i in range(mid):
        attacked[missiles[i]] = True
    total = 0
    length = 0
    for i in range(1, n + 1):
        if not attacked[i]:
            length += 1
        else:
            total += (length + 1) // (a + 1)
            length = 0
    total += (length + 1) // (a + 1)
    return total >= k

def solve(n: int, k: int, a: int, missiles: list[int]) -> int:
    lo, hi = 1, len(missiles)
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_place(n, k, a, missiles, mid):
            lo = mid + 1
        else:
            ans = mid
            hi = mid - 1
    return ans

def main():
    # 입력
    n, k, a = map(int, input().split())
    m = int(input().strip())
    missiles = list(map(int, input().split()))
    # 풀이
    result = solve(n, k, a, missiles)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
