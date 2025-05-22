import sys
input = sys.stdin.readline

def solve(d: int, stones: list[int], m: int) -> int:
    stones = [0] + sorted(stones) + [d]
    def feasible(M: int) -> bool:
        removed = 0
        last = 0  # index of last kept stone
        for i in range(1, len(stones)):
            if stones[i] - stones[last] < M:
                removed += 1
            else:
                last = i
        return removed <= m

    lo, hi = 0, d+1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            lo = mid
        else:
            hi = mid
    return lo

def main():
    # 입력
    d, n, m = map(int, input().split())
    stones = [int(input()) for _ in range(n)]
    # 풀이
    result = solve(d, stones, m)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
