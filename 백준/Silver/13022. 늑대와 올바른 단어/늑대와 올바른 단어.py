import sys
input = sys.stdin.readline

def solve(s: str) -> int:
    idx = 0
    L = len(s)
    while idx < L:
        if s[idx] != 'w':
            return 0
        # 개수
        n = 0
        while idx < L and s[idx] == 'w':
            n += 1
            idx += 1
        # o
        cnt = 0
        while idx < L and s[idx] == 'o':
            cnt += 1
            idx += 1
        if cnt != n:
            return 0
        # l
        cnt = 0
        while idx < L and s[idx] == 'l':
            cnt += 1
            idx += 1
        if cnt != n:
            return 0
        # f
        cnt = 0
        while idx < L and s[idx] == 'f':
            cnt += 1
            idx += 1
        if cnt != n:
            return 0
    return 1

def main():
    # 입력
    s = input().strip()
    # 풀이
    res = solve(s)
    # 출력
    print(res)

if __name__ == "__main__":
    main()
