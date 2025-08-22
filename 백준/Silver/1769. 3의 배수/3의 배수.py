import sys
input = sys.stdin.readline

def solve(s: str) -> tuple[int, bool]:
    cnt = 0

    while len(s) > 1:
        total = 0 
        for ch in s:
            total += ord(ch) - 48   # '0' == 48
        s = str(total)
        cnt += 1

    is_mul3 = s in ('0', '3', '6', '9')
    return cnt, is_mul3

def main():
    # 입력
    s = input().strip()

    # 풀이
    cnt, ok = solve(s)

    # 출력
    print(cnt)
    print('YES' if ok else 'NO')

if __name__ == "__main__":
    main()
