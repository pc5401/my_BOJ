import sys
input = sys.stdin.readline


def is_ok(n: int, idx: int, words: list[int]) -> int:
    word = words[idx]
    m = len(word)
    for i in range(idx+1, n):
        ok_word = False
        for j in range(m):
            if word[j] != words[i][j]:
                ok_word = True
                break
        
        if not ok_word:
            return 0

    return 1


def main():
    N = int(input())
    words = [input().rstrip() for _ in range(N)]
    words.sort(key=len)
    check_lst = [ 1 if is_ok(N, i, words) else 0 for i in range(N)]

    print(sum(check_lst))


if __name__ == "__main__":
    main()