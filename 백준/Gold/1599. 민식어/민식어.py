import sys
input = sys.stdin.readline

order = {
    "a": 0, "b": 1, "k": 2, "d": 3, "e": 4, "g": 5, "h": 6, "i": 7,
    "l": 8, "m": 9, "n": 10, "ng": 11, "o": 12, "p": 13, "r": 14,
    "s": 15, "t": 16, "u": 17, "w": 18, "y": 19
}

def key_minsik(word: str):
    res = []
    i = 0
    while i < len(word):
        if word[i] == 'n' and i + 1 < len(word) and word[i + 1] == 'g':
            res.append(order["ng"])
            i += 2
        else:
            res.append(order[word[i]])
            i += 1
    return tuple(res)

def solve(N, words):
    words.sort(key=key_minsik)
    return words

def main():
    # 입력
    N = int(input().strip())
    words = [input().strip() for _ in range(N)]

    # 풀이
    result = solve(N, words)

    # 출력
    print("\n".join(result))

if __name__ == "__main__":
    main()
