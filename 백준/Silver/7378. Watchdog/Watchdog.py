import sys
input = sys.stdin.readline

def solve(S, H, hatches):
    hatch_set = set(hatches)
    for x in range(S + 1):
        for y in range(S + 1):
            if (x, y) in hatch_set:
                continue
            r = min(x, y, S - x, S - y)
            r2 = r * r
            ok = True
            for hx, hy in hatches:
                dx = x - hx
                dy = y - hy
                d2 = dx * dx + dy * dy
                if d2 > r2:
                    ok = False
                    break
            if ok:
                return x, y
    return None

def main():
    # 입력
    T = int(input())
    cases = []
    for _ in range(T):
        S, H = map(int, input().split())
        hatches = [tuple(map(int, input().split())) for _ in range(H)]
        cases.append((S, H, hatches))

    # 풀이
    results = []
    for S, H, hatches in cases:
        ans = solve(S, H, hatches)
        results.append("poodle" if ans is None else f"{ans[0]} {ans[1]}")

    # 출력
    print("\n".join(results))

if __name__ == "__main__":
    main()
