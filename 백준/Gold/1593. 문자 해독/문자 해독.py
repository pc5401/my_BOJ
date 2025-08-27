import sys
input = sys.stdin.readline

def solve(g, W, S):
    n = len(S)
    if g > n:
        return 0

    def idx(ch):
        o = ord(ch)
        if 65 <= o <= 90:
            return o - 65
        return 26 + (o - 97)

    need = [0] * 52
    win = [0] * 52

    for ch in W:
        need[idx(ch)] += 1
    for i in range(g):
        win[idx(S[i])] += 1

    diff = 0
    for i in range(52):
        if need[i] != win[i]:
            diff += 1

    ans = 0
    if diff == 0:
        ans += 1

    for r in range(g, n):
        out = idx(S[r - g])
        before = (win[out] == need[out])
        win[out] -= 1
        after = (win[out] == need[out])
        if before and not after:
            diff += 1
        elif not before and after:
            diff -= 1

        inn = idx(S[r])
        before = (win[inn] == need[inn])
        win[inn] += 1
        after = (win[inn] == need[inn])
        if before and not after:
            diff += 1
        elif not before and after:
            diff -= 1

        if diff == 0:
            ans += 1

    return ans

def main():
    # 입력
    g, s_len = map(int, input().split())
    W = input().strip()
    S = input().strip()

    # 풀이
    result = solve(g, W, S)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
