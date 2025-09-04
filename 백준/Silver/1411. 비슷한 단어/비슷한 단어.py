import sys
input = sys.stdin.readline

def solve(N, words):
    def pattern(s):
        mp = {}
        nxt = 0
        seq = []
        for ch in s:
            if ch not in mp:
                mp[ch] = nxt
                nxt += 1
            seq.append(mp[ch])
        return tuple(seq)

    cnt = {}
    for w in words:
        key = pattern(w)
        cnt[key] = cnt.get(key, 0) + 1

    result = 0
    for c in cnt.values():
        result += c * (c - 1) // 2
    return result

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
