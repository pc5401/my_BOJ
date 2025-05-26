import sys
input = sys.stdin.readline

def solve(N: int, L: int, citations: list[int]) -> int:
    freq = [0] * (N + 1)
    for c in citations:
        freq[c if c <= N else N] += 1

    suf = [0] * (N + 2)
    for h in range(N, -1, -1):
        suf[h] = suf[h+1] + freq[h]
    
    def can(h: int) -> bool:
        k = suf[h]
        if k >= h:
            return True
        need = h - k
        t = freq[h-1] if h >= 1 else 0
        return need <= L and need <= t

    lo, hi = 0, N
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo

def main():
    # 입력
    N, L = map(int, input().split())
    citations = list(map(int, input().split()))
    # 풀이
    result = solve(N, L, citations)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
