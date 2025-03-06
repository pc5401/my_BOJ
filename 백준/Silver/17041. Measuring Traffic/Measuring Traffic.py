import sys
input = sys.stdin.readline

def solve(n: int, segs: list[tuple[str, int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    INF = 10**9
    lo, hi = 0, INF
    for typ, L, U in segs:
        if typ == "on":
            lo += L
            hi += U
        elif typ == "off":
            lo = max(lo - U, 0)
            hi = max(hi - L, 0)
        else:  # "none"
            lo = max(lo, L)
            hi = min(hi, U)
    final_range = (lo, hi)
    
    clo, chi = final_range
    for typ, L, U in reversed(segs):
        if typ == "on":
            clo = max(clo - U, 0)
            chi = chi - L
        elif typ == "off":
            clo = clo + L
            chi = chi + U
        else:  # "none"
            clo = max(clo, L)
            chi = min(chi, U)
    init_range = (clo, chi)
    return init_range, final_range

def main():
    # 입력
    n = int(input())
    segs = []
    for _ in range(n):
        parts = input().split()
        typ = parts[0]
        L, U = int(parts[1]), int(parts[2])
        segs.append((typ, L, U))
    
    # 풀이
    init_range, final_range = solve(n, segs)
    
    # 출력
    print(f"{init_range[0]} {init_range[1]}")
    print(f"{final_range[0]} {final_range[1]}")

if __name__ == "__main__":
    main()
