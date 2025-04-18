import sys
input = sys.stdin.readline

def solve(N: int, words: list[str]) -> int:
    char_entries = [[] for _ in range(26)]
    
    for idx, w in enumerate(words):
        L = len(w)
        min_x = [L] * 26
        min_y = [L] * 26
        for p, ch in enumerate(w):
            k = ord(ch) - ord('a')
            x = L - p - 1
            if x < min_x[k]:
                min_x[k] = x
            if p < min_y[k]:
                min_y[k] = p

        for k in range(26):
            if min_y[k] < L:  # 문자 k가 등장했으면
                char_entries[k].append((idx, min_x[k], min_y[k]))
    
    best = None
    for entries in char_entries:
        m = len(entries)
        if m < 2:
            continue
        x1 = x2 = None  # (value, id)
        y1 = y2 = None
        for (idx, x, y) in entries:
            if x1 is None or x < x1[0]:
                x2 = x1
                x1 = (x, idx)
            elif x2 is None or x < x2[0]:
                x2 = (x, idx)
            if y1 is None or y < y1[0]:
                y2 = y1
                y1 = (y, idx)
            elif y2 is None or y < y2[0]:
                y2 = (y, idx)

        if x1[1] != y1[1]:
            cand = x1[0] + y1[0]
        else:
            cand = min(x1[0] + y2[0], x2[0] + y1[0])
        if best is None or cand < best:
            best = cand
    
    return -1 if best is None else best

def main():
    # 입력
    N = int(input().strip())
    words = [input().strip() for _ in range(N)]
    # 풀이
    result = solve(N, words)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
