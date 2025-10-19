import sys
from fractions import Fraction

def solve(X, N, entries):
    cand = [(name, v) for name, v in entries if v * 20 >= X]
    if not cand:
        return []
    scores = []
    for name, v in cand:
        for d in range(1, 15):
            scores.append((Fraction(v, d), name))
    scores.sort(reverse=True)  # 큰 점수부터
    chips = {name: 0 for name, _ in cand}
    for i in range(min(14, len(scores))):
        _, name = scores[i]
        chips[name] += 1
    out = sorted(chips.items(), key=lambda x: x[0])
    return out

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    # 입력
    X = int(next(it))
    N = int(next(it))
    entries = []
    for _ in range(N):
        name = next(it)
        v = int(next(it))
        entries.append((name, v))
    # 풀이
    ans = solve(X, N, entries)
    # 출력
    for name, cnt in ans:
        print(name, cnt)

if __name__ == "__main__":
    main()
