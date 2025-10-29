import sys

def solve(N, K, words):
    base = 0
    for ch in "antic":
        base |= 1 << (ord(ch) - 97)

    if K < 5:
        return 0
    if K == 26:
        return N

    w_masks = []
    all_mask = 0
    for s in words:
        m = 0
        for ch in s.strip():
            m |= 1 << (ord(ch) - 97)
        w_masks.append(m)
        all_mask |= m

    candidates = []
    for i in range(26):
        b = 1 << i
        if (all_mask & b) and not (base & b):
            candidates.append(b)

    need = K - 5
    if need >= len(candidates):
        know = base
        for b in candidates:
            know |= b
        cnt = 0
        inv = ~know
        for wm in w_masks:
            if wm & inv == 0:
                cnt += 1
        return cnt

    best = 0

    def dfs(idx, picked, sel_mask):
        nonlocal best
        if len(candidates) - idx < need - picked:
            return
        if picked == need:
            know = base | sel_mask
            inv = ~know
            cnt = 0
            for wm in w_masks:
                if wm & inv == 0:
                    cnt += 1
            if cnt > best:
                best = cnt
            return
        if idx == len(candidates):
            return
        dfs(idx + 1, picked + 1, sel_mask | candidates[idx])
        dfs(idx + 1, picked, sel_mask)

    dfs(0, 0, 0)
    return best

def main():
    #입력
    input = sys.stdin.readline
    N, K = map(int, input().split())
    words = [input().strip() for _ in range(N)]
    #풀이
    ans = solve(N, K, words)
    #출력
    print(ans)

if __name__ == "__main__":
    main()
