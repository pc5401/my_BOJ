import sys

def solve(N, arr, K):
    max_len = max(len(s) for s in arr) if N > 0 else 0
    pow36 = [1] * (max_len + 1)
    for i in range(1, max_len + 1):
        pow36[i] = pow36[i - 1] * 36

    cnt = [[0] * max_len for _ in range(36)]
    total = 0

    for s in arr:
        L = len(s)
        for i, ch in enumerate(reversed(s)):
            if '0' <= ch <= '9':
                v = ord(ch) - ord('0')
            else:
                v = ord(ch) - ord('A') + 10
            total += v * pow36[i]
            cnt[v][i] += 1

    gains = []
    for d in range(36):
        w = 0
        for i in range(max_len):
            if cnt[d][i]:
                w += cnt[d][i] * pow36[i]
        gains.append((35 - d) * w)

    gains.sort(reverse=True)
    add = sum(gains[:K])
    total += add

    if total == 0:
        return "0"

    digits = []
    while total > 0:
        total, r = divmod(total, 36)
        if r < 10:
            digits.append(chr(ord('0') + r))
        else:
            digits.append(chr(ord('A') + (r - 10)))
    return ''.join(reversed(digits))

def main():
    #입력
    data = sys.stdin.read().strip().splitlines()
    N = int(data[0])
    arr = [data[i + 1].strip() for i in range(N)]
    K = int(data[N + 1])
    #풀이
    ans = solve(N, arr, K)
    #출력
    print(ans)

if __name__ == "__main__":
    main()
