import sys
input = sys.stdin.readline

def search(n: int) -> int:
    lo, hi = 0, 1259
    while lo <= hi:
        mid = (lo + hi) // 2
        m3 = mid * mid * mid
        if m3 == n:
            return mid
        if m3 < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

def solve(cases):
    out = []
    for i, (A, B) in enumerate(cases, 1):
        fb = search(B)
        fa = search(A)
        ca = fa if fa * fa * fa == A else fa + 1
        cnt = fb - ca + 1
        if cnt < 0:
            cnt = 0
        out.append(f"Case #{i}: {cnt}")
    return out

def main():
    # 입력
    T = int(input().strip())
    cases = [tuple(map(int, input().split())) for _ in range(T)]

    # 풀이
    result = solve(cases)

    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
