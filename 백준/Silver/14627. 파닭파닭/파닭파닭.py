import sys
input = sys.stdin.readline

def solve(S: int, C: int, L: list[int]) -> int:
    total = sum(L)
    lo, hi = 1, max(L)
    best = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = 0
        for l in L:
            cnt += l // mid

            if cnt >= C:
                break
        if cnt >= C:
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return total - best * C

def main():
    # 입력
    S, C = map(int, input().split())
    L = [int(input()) for _ in range(S)]
    # 풀이
    result = solve(S, C, L)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
