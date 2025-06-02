import sys
import bisect
input = sys.stdin.readline

def solve_row(values: list[int]) -> tuple[int,int,int]:
    L = len(values)
    max_ending = values[0]
    S = values[0]
    for x in values[1:]:
        max_ending = max(x, max_ending + x)
        S = max(S, max_ending)

    ps = [0]*(L+1)
    for i in range(1, L+1):
        ps[i] = ps[i-1] + values[i-1]
    d = {}
    for idx, val in enumerate(ps):
        d.setdefault(val, []).append(idx)
    best_len = L+1
    best_start = L+1
    for j in range(1, L+1):
        target = ps[j] - S
        if target in d:
            lst = d[target]
            # i < j
            pos = bisect.bisect_left(lst, j) - 1
            if pos >= 0:
                i = lst[pos]
                length = j - i
                start = i + 1
                if length < best_len or (length == best_len and start < best_start):
                    best_len = length
                    best_start = start
    
    end = best_start + best_len - 1
    return S, best_start, end

def main():
    # 입력
    n = int(input())
    rows = []
    for _ in range(n):
        L = int(input())
        vals = list(map(int, input().split()))
        rows.append(vals)
    # 풀이
    total = 0
    results = []
    for vals in rows:
        S, st, ed = solve_row(vals)
        total += S
        results.append((st, ed))
    # 출력
    print(total)
    for st, ed in results:
        print(st, ed)

if __name__ == "__main__":
    main()
